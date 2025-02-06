import sys

from PySide6.QtWidgets import QApplication

from app import NotesApp



def load_stylesheet():
    with open("app/styles/styles.qss", "r") as file:
        return file.read()


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet())
    window = NotesApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
