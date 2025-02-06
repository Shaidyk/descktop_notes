from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget, \
    QStackedWidget, QLabel, QLineEdit


class RegistrationScreen(QWidget):
    def __init__(self, signin_callback):
        super().__init__()

        self.signin_callback = signin_callback
        self.setWindowTitle('Notes - SignIn')

        layout = QVBoxLayout()

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
        self.login_button.clicked.connect(self.signin)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def signin(self):
        self.signin_callback()
