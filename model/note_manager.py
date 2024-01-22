import json
import csv
from datetime import datetime

class NoteManager:
    def __init__(self):
        self.notes = []

    # Остальные методы NoteManager здесь

    def add_image_to_note(self, note_id, image_path):
        for note in self.notes:
            if note.note_id == note_id:
                note.add_image(image_path)
                break

    def display_images_for_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                print(f"Images for Note {note.note_id}:")
                for image in note.images:
                    print(image)
                break
