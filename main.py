from model.note_manager import NoteManager
from view.note_view import NoteView
from view.menu_view import MenuView
from presenter.presenter import NotePresenter

if __name__ == "__main__":
    note_manager = NoteManager()
    note_view = NoteView()
    menu_view = MenuView()
    presenter = NotePresenter(note_view, menu_view, note_manager)

    presenter.run()
