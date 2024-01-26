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
                filter_choice = self.menu_view.get_filter_choice("Read")
                notes = self.note_manager.filter_notes(filter_choice)
                self.menu_view.read_notes(notes, filtered=(filter_choice != ""))
                note_id = self.menu_view.get_note_id()
                if note_id:
                    note = self.note_manager.get_note_by_id(int(note_id))
                    if note:
                        self.note_view.display_note(note)
                        input("Press Enter to return to the main menu...")

            elif choice == "3":
                notes = self.note_manager.read_notes()
                note_id = self.menu_view.edit_note(notes)
                if note_id:
                    edit_choice = self.menu_view.get_edit_choice()
                    if edit_choice == "1" or edit_choice == "2":
                        new_value = input(f"Enter the new {'Title' if edit_choice == '1' else 'Body'}: ")
                        self.note_manager.edit_note_by_id(int(note_id), edit_choice, new_value)
                        print("Note successfully edited.")
                    else:
                        print("Invalid edit choice. Note not edited.")

            elif choice == "4":
                notes = self.note_manager.read_notes()
                note_id = self.menu_view.delete_note(notes)
                if note_id:
                    self.note_manager.delete_note_by_id(int(note_id))
                    print("Note successfully deleted.")

            elif choice == "5":
                break
