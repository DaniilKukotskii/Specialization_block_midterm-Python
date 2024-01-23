class NoteView:
    def display_note(self, note):
        print(f"Note ID: {note.note_id}")
        print(f"Title: {note.title}")
        print(f"Body: {note.body}")
        print(f"Timestamp: {note.timestamp}")
