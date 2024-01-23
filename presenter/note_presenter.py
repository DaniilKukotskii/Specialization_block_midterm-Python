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
                notes = self.note_manager.read_notes()
                self.menu_view.read_notes(notes)
                note_id = self.menu_view.get_note_id()
                if note_id is not None:
                    note = self.note_manager.get_note_by_id(int(note_id))
                    if note:
                        self.note_view.display_note(note)

            elif choice == "3":
                notes = self.note_manager.read_notes()
                self.menu_view.read_notes(notes)
                note_id = self.menu_view.get_note_id()
                if note_id is not None:
                    new_title, new_body = self.menu_view.edit_note()
                    if new_title is not None and new_body is not None:
                        self.note_manager.edit_note_by_id(int(note_id), new_title, new_body)

            elif choice == "4":
                notes = self.note_manager.read_notes()
                self.menu_view.read_notes(notes)
                note_id = self.menu_view.get_note_id()
                if note_id is not None:
                    self.note_manager.delete_note_by_id(int(note_id))

            elif choice == "5":
                break
