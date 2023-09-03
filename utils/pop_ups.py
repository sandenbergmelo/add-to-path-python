from PySide6.QtWidgets import QMessageBox
from qdarktheme import load_stylesheet


def pop_up(title, txt, icon='information'):
    icons = {'information': QMessageBox.Information,
             'warning': QMessageBox.Warning,
             'critical': QMessageBox.Critical,
             'question': QMessageBox.Question,
             'no_icon': QMessageBox.NoIcon}

    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setIcon(icons[icon])
    msg.setText(txt)
    msg.setStyleSheet(load_stylesheet())
    msg.exec()
