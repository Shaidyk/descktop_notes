from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QStackedWidget

from app.screens import LandingScreen, LoginScreen, SignupScreen, NotesScreen


class NotesApp(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db

        self.setWindowTitle('Notes')
        self.resize(600, 400)
        self.center_window()

        self.stack = QStackedWidget()  # Контейнер для экранов
        self.setCentralWidget(self.stack)

        self.landing_screen = LandingScreen(self.show_login_screen, self.show_signup_screen)
        self.login_screen = LoginScreen(self.db, self.show_notes_screen)
        self.signup_screen = SignupScreen(self.db, self.show_notes_screen)
        self.notes_screen = NotesScreen(self.db, self.show_landing_screen)

        self.stack.addWidget(self.landing_screen)
        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.signup_screen)
        self.stack.addWidget(self.notes_screen)

    def show_landing_screen(self):
        self.stack.setCurrentWidget(self.landing_screen)

    def show_login_screen(self):
        self.stack.setCurrentWidget(self.login_screen)

    def show_signup_screen(self):
        self.stack.setCurrentWidget(self.signup_screen)

    def show_notes_screen(self):
        self.stack.setCurrentWidget(self.notes_screen)

    def center_window(self):
        """Центрирует окно на экране"""
        screen_geometry = QGuiApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)
