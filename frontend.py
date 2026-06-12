import flet as ft


def main(page: ft.Page):
    page.title = "Notes App"
    note_text_field = ft.TextField(label="Note text", hint_text="Enter note text")
    status_text = ft.Text("Welcome!")
    submit_btn = ft.ElevatedButton(content="Save note")
    page.add(note_text_field, submit_btn, status_text)


ft.run(main)
