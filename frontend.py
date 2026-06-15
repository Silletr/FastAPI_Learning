import flet as ft
from requests import post, get

API_URL = "http://127.0.0.1:8000"


async def main(page: ft.Page):
    note_name_field = ft.TextField()
    note_text_field = ft.TextField()

    def save_click(e):
        post(
            f"{API_URL}/notes",
            json={
                "note_name": note_name_field.value,
                "note_text": note_text_field.value,
            },
        )

    def show_notes(e):
        result = get(f"{API_URL}/notes")
        data = result.json()
        page.controls.clear()
        for note in data:
            page.add(
                ft.Text(f"Note Name: {note['note_name']}"),
                ft.Text(f"Note Text: {note['note_text']}\n"),
            )
            page.update()

    show_note = ft.Button("All Notes", on_click=show_notes)
    page.add(
        note_name_field,
        note_text_field,
        ft.Button("Save", on_click=save_click),
        show_note,
    )


ft.app(main)
