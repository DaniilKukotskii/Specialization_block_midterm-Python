class MenuView:
    def display_menu(self):
        print("1. Create Note")
        print("2. Read Notes")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Exit")

    def get_user_choice(self):
        return input("Enter your choice: ")

    def display_note_titles(self, note_titles):
        if note_titles:
            print("Available Note Titles:")
            for title in note_titles:
                print(f"- {title}")
        else:
            print("No notes available.")

    def create_note(self):
        title = input("Enter the title of the note: ")
        body = input("Enter the body of the note: ")
        return title, body

    def read_notes(self, note_titles):
        self.display_note_titles(note_titles)
        choice = input("Enter the title of the note to read: ")
        return choice

    def edit_note(self, note_titles):
        self.display_note_titles(note_titles)
        choice = input("Enter the title of the note to edit: ")
        new_title = input("Enter the new title: ")
        new_body = input("Enter the new body: ")
        return choice, new_title, new_body

    def delete_note(self, note_titles):
        self.display_note_titles(note_titles)
        choice = input("Enter the title of the note to delete: ")
        return choice
