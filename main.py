import sys

from PySide6.QtWidgets import QApplication

from app import NotesApp


def main():
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
