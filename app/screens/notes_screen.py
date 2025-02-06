from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QTreeWidget, QTreeWidgetItem, QHBoxLayout


class NotesScreen(QWidget):
    def __init__(self, db, landing_callback):
        super().__init__()
        self.db = db

        self.landing_callback = landing_callback

        self.setWindowTitle('Notes - Notes')

        # Основной макет (горизонтальный, чтобы слева было дерево)
        main_layout = QHBoxLayout()

        # Создаём дерево иерархии заметок
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Заметки")  # Заголовок дерева
        self.populate_tree()  # Заполняем дерево
        self.tree.itemClicked.connect(self.load_note)  # Обрабатываем клик по заметке

        main_layout.addWidget(self.tree)  # Добавляем дерево слева

        # Контейнер для заметки (справа)
        right_layout = QVBoxLayout()

        self.note_field = QTextEdit()
        right_layout.addWidget(self.note_field)

        self.logout_button = QPushButton("LogOut")
        self.logout_button.clicked.connect(self.logout)
        right_layout.addWidget(self.logout_button)

        # Добавляем правую часть в основной макет
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

        # Данные заметок
        self.notes = {
            "AWS": "AWS access keys: XXXX-XXXX",
            "Server": "Server credentials: XXXX-XXXX"
        }

    def populate_tree(self):
        """Заполняет дерево иерархии"""
        # Создаём корневой узел
        my_project = QTreeWidgetItem(self.tree, ["myproject"])

        # Ветка "keys"
        keys = QTreeWidgetItem(my_project, ["keys"])

        # Листовые элементы (заметки)
        aws = QTreeWidgetItem(keys, ["AWS"])
        server = QTreeWidgetItem(keys, ["Server"])

    def load_note(self, item):
        """Загружает текст заметки при клике"""
        note_name = item.text(0)  # Получаем имя заметки
        if note_name in self.notes:
            self.note_field.setText(self.notes[note_name])
        else:
            self.note_field.clear()

    def logout(self):
        """Выход в главное меню"""
        self.landing_callback()
