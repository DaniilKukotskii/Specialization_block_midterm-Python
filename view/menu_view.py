class MenuView:
    def display_menu(self):
        print("1. Create Note")
        print("2. Read Notes")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Exit")

    def get_user_choice(self):
        return input("Enter your choice: ")

    def read_notes(self, notes, filtered=False):
        if notes:
            print("Available Notes:")
            for note in notes:
                print(f"- {note.title} (ID: {note.note_id})")
            if filtered:
                print("Notes are filtered.")
            else:
                print("No notes available.")

    def create_note(self):
        title = input("Enter the title of the note (press Enter to return to the main menu): ")
        if not title:
            return None, None
        body = input("Enter the body of the note (press Enter to return to the main menu): ")
        return title, body

    def edit_note(self, notes):
        self.read_notes(notes)
        note_id = input("Enter the ID of the note to edit (press Enter to return to the main menu): ")
        return note_id if note_id.strip() else None

    def delete_note(self, notes):
        self.read_notes(notes)
        choice = input("Enter the ID of the note to delete (press Enter to return to the main menu): ")
        return choice if choice.strip() else None

    def get_note_id(self):
        note_id = input("Enter the ID of the note (press Enter to return to the main menu): ")
        return note_id if note_id.strip() else None

    def get_filter_choice(self, action):
        print(f"{action} Filter Options:")
        print("1. Sort by date (from new to old)")
        print("2. Sort by date (from old to new)")
        return input("Enter your choice (press Enter to skip): ")

    def get_edit_choice(self):
        print("Edit Options:")
        print("1. Edit Title")
        print("2. Edit Body")
        return input("Enter your choice (press Enter to skip): ")
