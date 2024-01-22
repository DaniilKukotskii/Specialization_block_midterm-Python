class MenuView:
    def display_menu(self):
        print("1. Create Note")
        print("2. Read Notes")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Save to JSON")
        print("6. Save to CSV")
        print("7. Exit")

    def get_user_choice(self):
        return input("Enter your choice: ")
