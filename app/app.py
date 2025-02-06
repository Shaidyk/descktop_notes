from PySide6.QtWidgets import QMainWindow, QStackedWidget

from app.screens import LandingScreen, LoginScreen, RegistrationScreen, NotesScreen


class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.setWindowTitle('Notes')
        self.setGeometry(100, 100, 600, 400)

        self.stack = QStackedWidget()  # Контейнер для экранов
        self.setCentralWidget(self.stack)

        self.landing_screen = LandingScreen(self.show_login_screen, self.show_signin_screen)
        self.login_screen = LoginScreen(self.show_notes_screen)
        self.signin_screen = RegistrationScreen(self.show_notes_screen)
        self.notes_screen = NotesScreen(self.show_landing_screen)

        self.stack.addWidget(self.landing_screen)
        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.signin_screen)
        self.stack.addWidget(self.notes_screen)

    def show_landing_screen(self):
        self.stack.setCurrentWidget(self.landing_screen)

    def show_login_screen(self):
        self.stack.setCurrentWidget(self.login_screen)

    def show_signin_screen(self):
        self.stack.setCurrentWidget(self.signin_screen)

    def show_notes_screen(self):
        self.stack.setCurrentWidget(self.notes_screen)
