from os import getenv

import flet as ft

HOME = f'{getenv("HOME")}/'


def add_to_path():
    pass


def main(page: ft.Page):
    page.title = 'Add to Path'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_max_width = 500
    page.window_max_height = 200

    def add_to_field(e: ft.FilePickerResultEvent):
        directory_path.value = e.path
        page.update()

    directory_path = ft.TextField()
    folder_picker = ft.FilePicker(on_result=add_to_field)

    page.add(folder_picker)
    page.add(
        ft.Row(
            [ft.Text('Pasta: ', size=24), directory_path,
             ft.IconButton(icon=ft.icons.FOLDER, icon_size=40,
                           on_click=lambda _: folder_picker.get_directory_path(
                               initial_directory=HOME,
                               dialog_title='Escolha a pasta para adicionar'
                           ))]
        ),
        ft.Row(
            [ft.ElevatedButton(content=ft.Text('Adicionar ao PATH', size=24))],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.padding = 10
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
