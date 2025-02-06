import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from passlib.hash import bcrypt
from contextlib import contextmanager

from app.models.models import Base, User, Project, Folder, Note  # Импорт моделей


# Путь к базе данных
DATABASE_URL = "sqlite:///notes.db"


class DatabaseManager:
    def __init__(self):
        """Создаёт подключение к базе и проверяет её существование"""
        self.engine = create_engine(DATABASE_URL, echo=False)
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

        if not os.path.exists("notes.db"):
            print("⚠️  База данных не найдена, создаём новую...")
            self.create_database()
        else:
            print("✅ База данных уже существует")

        self.ensure_tables_exist()

    def create_database(self):
        """Создаёт базу данных и таблицы"""
        Base.metadata.create_all(bind=self.engine)
        print("✅ Таблицы БД созданы")

    def ensure_tables_exist(self):
        """Проверяет, есть ли таблицы в БД, и создаёт их, если нет"""
        with self.engine.connect() as connection:
            try:
                # Проверяем, есть ли таблицы в базе
                result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';")).fetchall()
                if not result:
                    print("⚠️  В базе данных нет таблиц, создаём их...")
                    self.create_database()
                else:
                    print("✅ Таблицы БД уже существуют")
            except OperationalError:
                print("❌ Ошибка при проверке БД, возможно, файл повреждён")

    @contextmanager
    def get_session(self):
        """Менеджер контекста для работы с сессией"""
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    # --- Регистрация и авторизация ---
    def create_user(self, username, password):
        """Создаёт нового пользователя"""
        with self.get_session() as session:
            existing_user = session.query(User).filter_by(username=username).first()
            if existing_user:
                print("❌ Пользователь уже существует!")
                return None  # Возвращаем None, если пользователь есть

            hashed_password = bcrypt.hash(password)
            user = User(username=username, password_hash=hashed_password)
            session.add(user)
            session.commit()
            return user

    def authenticate_user(self, username, password):
        """Проверяет логин и пароль"""
        with self.get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            if user and bcrypt.verify(password, user.password_hash):
                return user.id
            return None

    # --- Работа с проектами ---
    def create_project(self, user_id, name):
        """Создаёт проект"""
        with self.get_session() as session:
            project = Project(user_id=user_id, name=name)
            session.add(project)
            return project

    def get_projects(self, user_id):
        """Возвращает все проекты пользователя"""
        with self.get_session() as session:
            return session.query(Project).filter_by(user_id=user_id).all()

    # --- Работа с папками ---
    def create_folder(self, project_id, name, parent_folder_id=None):
        """Создаёт папку"""
        with self.get_session() as session:
            folder = Folder(project_id=project_id, name=name, parent_folder_id=parent_folder_id)
            session.add(folder)
            return folder

    def get_folders(self, project_id, parent_folder_id=None):
        """Возвращает список папок в проекте"""
        with self.get_session() as session:
            return session.query(Folder).filter_by(project_id=project_id, parent_folder_id=parent_folder_id).all()

    # --- Работа с заметками ---
    def create_note(self, folder_id, title, content):
        """Создаёт заметку"""
        with self.get_session() as session:
            note = Note(folder_id=folder_id, title=title, content=content)
            session.add(note)
            return note

    def get_notes(self, folder_id):
        """Возвращает заметки в папке"""
        with self.get_session() as session:
            return session.query(Note).filter_by(folder_id=folder_id).all()
