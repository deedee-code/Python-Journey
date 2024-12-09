from view_books import view_available_books
from borrow_books import borrow_a_book
from returns_books import return_a_book

list_of_books = ['Python Basics', 'Data Science 101', 'AI for Beginners']

def library_management_system():
    print("Welcome to the Library Management System")
    
    while True:
        print("\nOptions:")
        print("1. View Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            view_available_books(list_of_books)
        elif choice == '2':
            borrowed_books = []
            borrow_a_book(list_of_books, borrowed_books)
        elif choice == '3':
            return_a_book(list_of_books, borrowed_books)
        elif choice == '4':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library_management_system()