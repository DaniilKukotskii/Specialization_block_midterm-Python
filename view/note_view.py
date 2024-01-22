class NoteView:
    def display_notes(self, notes):
        for note in notes:
            print(f"ID: {note.note_id}\nTitle: {note.title}\nBody: {note.body}\nTimestamp: {note.timestamp}\n{'='*30}")

    def display_message(self, message):
        print(message)

    def get_user_input(self, prompt):
        return input(prompt)
