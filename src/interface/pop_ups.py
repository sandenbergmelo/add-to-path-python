from flet import AlertDialog, MainAxisAlignment, Page, Text, TextButton


def pop_up(page: Page, title: str, txt: str):
    def _close(e):
        msg.open = False
        page.update()

    msg = AlertDialog(
        title=Text(title),
        content=Text(txt),
        actions=[
            TextButton("Ok", on_click=_close),
        ],
        actions_alignment=MainAxisAlignment.END,
    )

    page.dialog = msg
    msg.open = True
    page.update()
