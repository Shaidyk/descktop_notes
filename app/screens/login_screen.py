from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget, \
    QStackedWidget, QLabel, QLineEdit


class LoginScreen(QWidget):
    def __init__(self, login_callback):
        super().__init__()

        self.login_callback = login_callback
        self.setWindowTitle('Notes - LogIn')

        layout = QVBoxLayout()

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
