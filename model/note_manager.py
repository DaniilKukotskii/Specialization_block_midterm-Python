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
                notes = []

                for row in reader:
                    try:
                        note_id = int(row['note_id'])
                        title = row['title']
                        body = row['body']
                        timestamp = row['timestamp']
                        new_note = Note(note_id, title, body, timestamp)
                        notes.append(new_note)
                    except (ValueError, KeyError):
                        print("Error loading note:", row)

        except FileNotFoundError:
            print("Файл не найден")
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
        if not title or not body:
            print("Note creation cancelled.")
            return
        note_id = len(self.notes) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, body, timestamp)
        self.notes.append(new_note)
        self.save_to_csv()

    def filter_notes(self, filter_choice):
        if filter_choice == "1":
            return sorted(self.notes, key=lambda x: x.timestamp, reverse=True)
        elif filter_choice == "2":
            return sorted(self.notes, key=lambda x: x.timestamp)
        else:
            return self.notes

    def read_notes(self):
        return self.notes

    def edit_note_by_id(self, note_id, edit_choice, new_value):
        for note in self.notes:
            if note.note_id == note_id:
                if edit_choice == "1":
                    note.title = new_value
                elif edit_choice == "2":
                    note.body = new_value
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_to_csv()
                break

    def delete_note_by_id(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_to_csv()

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None
