from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget, \
    QStackedWidget, QLabel


class LandingScreen(QWidget):
    def __init__(self, login_callback, signin_callback):
        super().__init__()

        self.login_callback = login_callback
        self.signin_callback = signin_callback

        layout = QVBoxLayout()

        self.label = QLabel("LogIn or Registration", alignment=Qt.AlignCenter)
        layout.addWidget(self.label)

        self.login_button = QPushButton("LogIn")
        self.login_button.clicked.connect(self.login)
        self.signin_button = QPushButton("SignIn")
        self.signin_button.clicked.connect(self.signin)

        layout.addWidget(self.login_button)
        layout.addWidget(self.signin_button)

        self.setLayout(layout)

    def login(self):
        self.login_callback()

    def signin(self):
        self.signin_callback()