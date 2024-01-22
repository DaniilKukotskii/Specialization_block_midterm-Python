from model.note_manager import NoteManager
from view.note_view import NoteView
from view.menu_view import MenuView


class NotePresenter:
    def __init__(self, note_view, menu_view, note_manager):
        self.note_view = note_view
        self.menu_view = menu_view
        self.note_manager = note_manager

    def run(self):
        while True:
            self.menu_view.display_menu()
            choice = self.menu_view.get_user_choice()

            # Остальной код NotePresenter здесь
