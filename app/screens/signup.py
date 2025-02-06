from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget, \
    QStackedWidget, QLabel, QLineEdit


class SignupScreen(QWidget):
    def __init__(self, signup_callback):
        super().__init__()

        self.signup_callback = signup_callback
        self.setWindowTitle('Notes - SignUp')

        layout = QVBoxLayout()
        self.set_layout_styles(layout)

        self.login_label = QLabel("Login:")
        layout.addWidget(self.login_label)
        self.login_field = QLineEdit()
        layout.addWidget(self.login_field)

        self.password_label = QLabel("Password:")
        layout.addWidget(self.password_label)
        self.password_field = QLineEdit()
        layout.addWidget(self.password_field)

        self.password2_label = QLabel("Password again:")
        layout.addWidget(self.password2_label)
        self.password2_field = QLineEdit()
        layout.addWidget(self.password2_field)

        self.login_button = QPushButton("Complete")
        self.login_button.clicked.connect(self.signup)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def signup(self):
        self.signup_callback()

    def set_layout_styles(self, layout):  # noqa
        layout.setSpacing(10)  # Отступы между элементами
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем всё
        layout.setContentsMargins(40, 40, 40, 40)  # Внешние отступы
        return layout
