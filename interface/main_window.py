from os import getenv, system
from pathlib import Path

from PySide6.QtWidgets import QFileDialog, QMainWindow

from interface.UI_main_window import Ui_MainWindow
from utils.pop_ups import pop_up


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def choose_directory(self):
        directory_path = QFileDialog.getExistingDirectory(
            caption='Escolher pasta',
            dir=getenv('HOME'),
        )

        self.txtPath.setText(directory_path)

    def add_to_path(self):
        HOME = getenv('HOME')
        directory_path = str(self.txtPath.text()).strip()
        profiles = [f'{HOME}/.profile',
                    f'{HOME}/.bash_profile',
                    f'{HOME}/.zprofile']

        if directory_path == '':
            pop_up('ERRO!', 'Caminho vazio!', 'warning')
            return False

        if not Path(directory_path).is_dir():
            pop_up('ERRO!', 'O caminho informado não é uma pasta.', 'warning')
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
            pop_up('ERRO!', 'A pasta já está adicionada ao PATH.', 'warning')
            return False

        try:
            for i, profile in enumerate(profiles):
                if not is_in_path[i]:
                    system(f'{command} >> {profile}')

            pop_up(
                'Sucesso!', 'A pasta foi adicionada ao PATH com sucesso!', 'information')
            self.txtPath.setText('')
            return True
        except Exception as err:
            print(err.__class__)
            pop_up('ERRO!', 'Ocorreu um erro ao adicionar a pasta ao PATH.', 'critical')
            return False
