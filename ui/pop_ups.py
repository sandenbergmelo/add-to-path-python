from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from qdarktheme import load_stylesheet


def pop_up_info(titulo, texto):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setIcon(QMessageBox.Information)
    msg.setText(texto)
    msg.setStyleSheet(load_stylesheet())
    msg.exec()


def pop_up_warning(titulo, texto):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setIcon(QMessageBox.Warning)
    msg.setText(texto)
    msg.setStyleSheet(load_stylesheet())
    msg.exec()

def pop_up_critical(titulo, texto):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setIcon(QMessageBox.Critical)
    msg.setText(texto)
    msg.setStyleSheet(load_stylesheet())
    msg.exec()
