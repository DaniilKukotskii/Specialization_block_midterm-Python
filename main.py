from presenter.note_presenter import NotePresenter
from view.menu_view import MenuView
from view.note_view import NoteView
from model.note_manager import NoteManager

if __name__ == "__main__":
    file_path = "notes.csv"
    note_manager = NoteManager(file_path)
    note_view = NoteView()
    menu_view = MenuView()
    presenter = NotePresenter(note_view, menu_view, note_manager)

    presenter.run()
