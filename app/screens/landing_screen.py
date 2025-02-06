from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget, \
    QStackedWidget, QLabel


class LandingScreen(QWidget):
    def __init__(self, login_callback, signup_callback):
        super().__init__()

        self.login_callback = login_callback
        self.signup_callback = signup_callback

        layout = QVBoxLayout()
        self.set_layout_styles(layout)


        self.label = QLabel("LogIn or SignUp")
        layout.addWidget(self.label)

        self.login_button = QPushButton("LogIn")
        self.login_button.clicked.connect(self.login)
        self.signup_button = QPushButton("SignUp")
        self.signup_button.clicked.connect(self.signup)

        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

    def login(self):
        self.login_callback()

    def signup(self):
        self.signup_callback()

    def set_layout_styles(self, layout):  # noqa
        layout.setSpacing(10)  # Отступы между элементами
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем всё
        layout.setContentsMargins(40, 40, 40, 40)  # Внешние отступы
        return layout