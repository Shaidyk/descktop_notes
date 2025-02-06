from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget, \
    QStackedWidget, QLabel


class NotesScreen(QWidget):
    def __init__(self, landing_callback):
        super().__init__()

        self.landing_callback = landing_callback

        self.setWindowTitle('Notes - Notes')

        layout = QVBoxLayout()

        self.login_button = QPushButton("LogOut")
        self.login_button.clicked.connect(self.logout)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def logout(self):
        self.landing_callback()
