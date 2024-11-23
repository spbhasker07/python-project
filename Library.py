import pickle as pic,os
print("=" * 45)
print("Library Management System".center(45))
print("=" * 45)
STORY_BOOK_FILE = "story_books.pkl"
SCIENCE_BOOK_FILE = "science_books.pkl"
ISSUED_BOOK_FILE = "issued_books.pkl"
RETURNED_BOOK_FILE = "returned_books.pkl"
default_story_book_list = {
    'Harry Potter and the Sorcerer’s Stone': 3,
    'Pride and Prejudice': 5,
    'Wuthering Heights': 2,
    'The Merchant of Venice': 4
}
default_science_book_list = {
    'Big Bang': 3,
    'A Brief History of Time': 2,
    'Cosmos': 5,
    'Alcohol in Space: Past, Present and Future': 1,
    'Silent Spring': 4
}
issued = {}
return_book = {}
def initialize_file(file_path, default_data):
    if not os.path.exists(file_path):
        with open(file_path, "wb") as file:
            pic.dump(default_data, file)
def load_data(file_path):
    with open(file_path, "rb") as file:
        return pic.load(file)
def save_data(file_path, data):
    with open(file_path, "wb") as file:
        pic.dump(data, file)
initialize_file(STORY_BOOK_FILE, default_story_book_list)
initialize_file(SCIENCE_BOOK_FILE, default_science_book_list)
initialize_file(ISSUED_BOOK_FILE, {})
initialize_file(RETURNED_BOOK_FILE, {})
# Load data
default_story_book_list = load_data(STORY_BOOK_FILE)
default_science_book_list = load_data(SCIENCE_BOOK_FILE)
issued = load_data(ISSUED_BOOK_FILE)
return_book = load_data(RETURNED_BOOK_FILE)
def see():
    while True:
        print("\n1. Story Books\n2. Science Books\n3. Exit")
        try:
            option = int(input("Enter your choice (1, 2, 3): "))
            if option == 1:
                print("\nAvailable Story Books:")
                for book, qty in default_story_book_list.items():
                    print(f"-- {book} (Quantity: {qty})")
            elif option == 2:
                print("\nAvailable Science Books:")
                for book, qty in default_science_book_list.items():
                    print(f"-- {book} (Quantity: {qty})")
            elif option == 3:
                print("Exiting the book viewing system.")
                break
            else:
                print("Invalid option. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def search():
    book_name = input("Enter the book name: ").strip()
    if book_name in default_story_book_list or book_name in default_science_book_list:
        print(f"Yes, the book '{book_name}' is available.")
    else:
        print(f"Sorry, the book '{book_name}' is not available.")
def add():
    while True:
        print("\n1. Add to Story Books\n2. Add to Science Books\n3. Exit")
        try:
            choice = int(input("Enter your choice (1, 2, 3): "))
            if choice in [1, 2]:
                book_name = input("Enter the book name: ").strip()
                quantity = int(input("Enter the quantity: "))
                if choice == 1:
                    default_story_book_list[book_name] = default_story_book_list.get(book_name, 0) + quantity
                    save_data(STORY_BOOK_FILE, default_story_book_list)
                    print(f"'{book_name}' has been added to Story Books.")
                elif choice == 2:
                    default_science_book_list[book_name] = default_science_book_list.get(book_name, 0) + quantity
                    save_data(SCIENCE_BOOK_FILE, default_science_book_list)
                    print(f"'{book_name}' has been added to Science Books.")
            elif choice == 3:
                print("Exiting the Add Book System.")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter valid details.")
def remove_book():
    book_name = input("Enter the book name to remove: ").strip()
    if book_name in default_story_book_list:
        del default_story_book_list[book_name]
        save_data(STORY_BOOK_FILE, default_story_book_list)
        print(f"The book '{book_name}' has been removed from Story Books.")
    elif book_name in default_science_book_list:
        del default_science_book_list[book_name]
        save_data(SCIENCE_BOOK_FILE, default_science_book_list)
        print(f"The book '{book_name}' has been removed from Science Books.")
    else:
        print(f"The book '{book_name}' is not available in the library.")
def issue_book():
    book_name = input("Enter the book name to issue: ").strip()
    if book_name in default_story_book_list or book_name in default_science_book_list:
        student_name = input("Enter the student name: ").strip()
        issued[book_name] = student_name
        save_data(ISSUED_BOOK_FILE, issued)
        print(f"The book '{book_name}' has been issued to {student_name}.")
    else:
        print(f"The book '{book_name}' is not available in the library.")
def return_book():
    book_name = input("Enter the book name to return: ").strip()
    student_name = input("Enter the student name: ").strip()
    if issued.get(book_name) == student_name:
        return_book[book_name] = student_name
        del issued[book_name]
        save_data(RETURNED_BOOK_FILE, return_book)
        save_data(ISSUED_BOOK_FILE, issued)
        print(f"The book '{book_name}' has been successfully returned by {student_name}.")
    else:
        print(f"No record found for '{book_name}' issued to {student_name}.")
# Menu
while True:
    print("\nLibrary Management System")
    print("1. See Available Books")
    print("2. Search a Book")
    print("3. Add a Book")
    print("4. Remove a Book")
    print("5. Issue a Book")
    print("6. Return a Book")
    print("7. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            see()
        elif choice == 2:
            search()
        elif choice == 3:
            add()
        elif choice == 4:
            remove_book()
        elif choice == 5:
            issue_book()
        elif choice == 6:
            return_book()
        elif choice == 7:
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 7.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
