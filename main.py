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
        directory=getenv('HOME')
    )

    window.txtPath.setText(directory_path)


def add_to_path():
    HOME = getenv('HOME')
    directory_path = str(window.txtPath.text()).strip()
    profiles = [f'{HOME}/.profile',
                f'{HOME}/.bash_profile',
                f'{HOME}/.zprofile']

    if directory_path == '':
        pop_up_warning('ERRO!', 'Caminho vazio!')
        return False

    if not Path(directory_path).is_dir():
        pop_up_warning('ERRO!', 'O caminho informado não é uma pasta.')
        return False

    path = '/' + directory_path.strip('/')
    if path.startswith(HOME):
        path = f'$HOME{path.removeprefix(HOME)}'

    line_to_put = f'export PATH=\"$PATH:{path}\"'
    command = f'echo \'{line_to_put}\''

    is_in_path = [False, False, False]

    for i, profile in enumerate(profiles):
        dot_profile_path = Path(profile)
        if not dot_profile_path.is_file():
            dot_profile_path.touch()

        with open(profile, 'r') as dot_profile_file:
            for line in dot_profile_file:
                if line.removesuffix('\n') == line_to_put:
                    is_in_path[i] = True
                    break

    if all(is_in_path):
        pop_up_warning('ERRO!', 'A pasta informada já está no PATH.')
        return False

    try:
        for i, profile in enumerate(profiles):
            if not is_in_path[i]:
                system(f'{command} >> {profile}')

        pop_up_info('Feito!', 'Diretório adicionado ao PATH com sucesso!')
        window.txtPath.setText('')
        return True
    except Exception as err:
        print(err.__class__)
        pop_up_critical('ERRO!', 'Um erro inesperado ocorreu!')
        return False


window = uic.loadUi('ui/main.ui')

window.btnDirectory.clicked.connect(choose_directory)
window.btnAdd.clicked.connect(add_to_path)

window.show()

app.exec()
