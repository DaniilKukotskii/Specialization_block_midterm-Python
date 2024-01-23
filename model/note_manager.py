import csv
from datetime import datetime
from .note import Note


class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = self.load_from_csv()

    def load_from_csv(self):
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file, delimiter=';')
                notes = [Note(int(row['note_id']), row['title'], row['body'], row['timestamp']) for row in reader]
        except FileNotFoundError:
            notes = []
        return notes

    def save_to_csv(self):
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['note_id', 'title', 'body', 'timestamp']
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for note in self.notes:
                writer.writerow({'note_id': note.note_id, 'title': note.title, 'body': note.body, 'timestamp': note.timestamp})

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, body, timestamp)
        self.notes.append(new_note)
        self.save_to_csv()

    def read_notes(self):
        return self.notes

    def edit_note_by_title(self, title, new_title, new_body):
        for note in self.notes:
            if note.title == title:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_to_csv()
                break

    def delete_note_by_title(self, title):
        self.notes = [note for note in self.notes if note.title != title]
        self.save_to_csv()
