from pathlib import Path
from os import getenv, system

from PyQt5 import QtWidgets, uic
from qdarktheme import load_stylesheet

from ui.pop_ups import *

app = QtWidgets.QApplication([])
app.setStyleSheet(load_stylesheet())


def choose_directory():
    directory_path = QtWidgets.QFileDialog.getExistingDirectory(
        caption='Escolher pasta',
        directory=getenv('HOME'),
    )

    window.txtPath.setText(directory_path)


def add_to_path():
    directory_path = str(window.txtPath.text()).strip()
    HOME = getenv('HOME')

    if directory_path == '':
        pop_up_warning('ERRO!', 'Caminho vazio!')
        return False

    if not Path(directory_path).is_dir():
        pop_up_warning('ERRO!', 'O caminho informado não é uma pasta')
        return False

    relative_path = directory_path.removeprefix(HOME)

    if directory_path.startswith(HOME):
        relative_path = f'$HOME{relative_path}'

    command = f'echo \'export PATH=\"$PATH:{relative_path}\"\''

    try:
        system(f'{command} >> ~/.profile')
        system(f'{command} >> ~/.zprofile')
        system(f'{command} >> ~/.bash_profile')
        
        pop_up_info('Feito!', 'Diretório adicionado ao PATH com sucesso')
    except Exception as err:
        print(err.__class__)
        pop_up_critical('ERRO!', 'Um erro inesperado ocorreu!')


window = uic.loadUi('ui/main.ui')

window.btnDirectory.clicked.connect(choose_directory)
window.btnAdd.clicked.connect(add_to_path)

window.show()

app.exec()
