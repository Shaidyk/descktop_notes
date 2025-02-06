from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget, \
    QStackedWidget, QLabel, QLineEdit
from PySide6.QtCore import Qt


class LoginScreen(QWidget):
    def __init__(self, db, login_callback):
        super().__init__()
        self.db = db

        self.login_callback = login_callback
        self.setWindowTitle('Notes - LogIn')

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

        self.login_button = QPushButton("LogIn")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        self.login_callback()

    def set_layout_styles(self, layout):  # noqa
        layout.setSpacing(10)  # Отступы между элементами
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем всё
        layout.setContentsMargins(40, 40, 40, 40)  # Внешние отступы
        return layout
