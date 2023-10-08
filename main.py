import flet as ft


def main(page: ft.Page):
    page.title = 'Add to Path'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_max_width = 500
    page.window_max_height = 200

    page.add(
        ft.Row(
            [ft.Text('Pasta: ', size=24), ft.TextField(),
             ft.IconButton(icon=ft.icons.FOLDER, icon_size=40)]
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
