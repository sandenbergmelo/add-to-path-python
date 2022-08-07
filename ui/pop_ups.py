from PyQt5.QtWidgets import QMessageBox
from qdarktheme import load_stylesheet


class Popup:
    def info(self, title, txt):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Information)
        msg.setText(txt)
        msg.setStyleSheet(load_stylesheet())
        msg.exec()

    def warning(self, title, txt):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(txt)
        msg.setStyleSheet(load_stylesheet())
        msg.exec()

    def critical(self, title, txt):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(txt)
        msg.setStyleSheet(load_stylesheet())
        msg.exec()
