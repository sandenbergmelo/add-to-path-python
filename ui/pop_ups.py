from PyQt5.QtWidgets import QMessageBox
from qdarktheme import load_stylesheet


def pop_up_info(title, txt):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Information)
    msg.setText(txt)
    msg.setStyleSheet(load_stylesheet())
    msg.exec()


def pop_up_warning(title, txt):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Warning)
    msg.setText(txt)
    msg.setStyleSheet(load_stylesheet())
    msg.exec()


def pop_up_critical(title, txt):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Critical)
    msg.setText(txt)
    msg.setStyleSheet(load_stylesheet())
    msg.exec()
