from sys import argv

from PySide6.QtWidgets import QApplication

from interface.main_window import MainWindow


def main():
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
