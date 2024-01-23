from view.menu_view import MenuView
from view.note_view import NoteView
from model.note_manager import NoteManager


class NotePresenter:
    def __init__(self, note_view, menu_view, note_manager):
        self.note_view = note_view
        self.menu_view = menu_view
        self.note_manager = note_manager

    def run(self):
        while True:
            self.menu_view.display_menu()
            choice = self.menu_view.get_user_choice()

            if choice == "1":
                title, body = self.menu_view.create_note()
                self.note_manager.add_note(title, body)

            elif choice == "2":
                note_titles = [note.title for note in self.note_manager.read_notes()]
                self.menu_view.read_notes(note_titles)

            elif choice == "3":
                note_titles = [note.title for note in self.note_manager.read_notes()]
                note_title = self.menu_view.edit_note(note_titles)
                new_title, new_body = self.menu_view.create_note()
                self.note_manager.edit_note_by_title(note_title, new_title, new_body)

            elif choice == "4":
                note_titles = [note.title for note in self.note_manager.read_notes()]
                note_title = self.menu_view.delete_note(note_titles)
                self.note_manager.delete_note_by_title(note_title)

            elif choice == "5":
                break
