import flet as ft
from datetime import datetime
import time
import threading


def main(page: ft.Page):
    page.title = "o'clock"
    greet_label = ft.Text(value="", size=20)
    time_label = ft.Text(value="00:00:00", size=60)

    try:
        from jnius import autoclass
        Stack = autoclass("java.util.Stack")
        stack = Stack()
        stack.push("O'CLOCK")

        stack_output = []
        while not stack.empty():
            stack_output.append(stack.pop())
        stack_output.reverse()

        greet_label.value = "\n".join(stack_output)
    except:
        greet_label.value = "O'CLOCK!"

    def update_time():
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            time_label.value = current_time
            page.update()
            time.sleep(1)

    threading.Thread(target=update_time, daemon=True).start()

    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[
                    ft.Container(
                        greet_label,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        time_label,
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            expand=True,
        )
    )


ft.app(main)
