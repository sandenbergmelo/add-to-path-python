from os import getenv, system
from pathlib import Path

import flet as ft


def main(page: ft.Page):
    HOME = f'{getenv("HOME")}/'

    page.title = 'Add to Path'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_max_width = 500
    page.window_max_height = 200

    def add_to_field(e: ft.FilePickerResultEvent):
        path_field.value = e.path
        page.update()

    def add_to_path(directory_path):
        HOME = getenv("HOME")

        profiles = [f'{HOME}/.profile',
                    f'{HOME}/.bash_profile',
                    f'{HOME}/.zprofile']

        if not directory_path:
            # pop_up('ERRO!', 'Caminho vazio!', 'warning')
            return False

        if not Path(directory_path).is_dir():
            # pop_up('ERRO!', 'O caminho informado não é uma pasta.', 'warning')
            return False

        path: str = '/' + directory_path.strip('/')
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
            # pop_up('ERRO!', 'A pasta já está adicionada ao PATH.', 'warning')
            return False

        try:
            for i, profile in enumerate(profiles):
                if not is_in_path[i]:
                    system(f'{command} >> {profile}')

            # pop_up(
            #     'Sucesso!', 'A pasta foi adicionada ao PATH com sucesso!', 'information')
            path_field.value = ''
            return True
        except Exception as err:
            print(err.__class__)
            # pop_up('ERRO!', 'Ocorreu um erro ao adicionar a pasta ao PATH.', 'critical')
            return False

    path_field = ft.TextField()
    folder_picker = ft.FilePicker(on_result=add_to_field)

    page.add(folder_picker)
    page.add(
        ft.Row(
            [ft.Text('Pasta: ', size=24), path_field,
             ft.IconButton(icon=ft.icons.FOLDER, icon_size=40,
                           on_click=lambda _: folder_picker.get_directory_path(
                               initial_directory=HOME,
                               dialog_title='Escolha a pasta para adicionar'
                           ))]
        ),
        ft.Row(
            [ft.ElevatedButton(
                content=ft.Text('Adicionar ao PATH', size=24),
                on_click=lambda _: add_to_path(path_field.value))],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.padding = 10
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
