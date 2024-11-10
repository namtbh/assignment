# Book Management System

class BookManagementSystem:
    def __init__(self):
        # Book database (ID: Title)
        self.books = {
            1: "Moby Dick",
            2: "The Great Gatsby",
            3: "1984",
            4: "To Kill a Mockingbird",
            5: "The Catcher in the Rye",
            6: "Pride and Prejudice",
            7: "The Lord of the Rings",
            8: "The Hobbit",
            9: "Harry Potter and the Philosopher's Stone",
            10: "War and Peace"
        }
        # List to store borrowed book IDs
        self.borrowed_books = []

    def list_books_on_loan(self):
        if not self.borrowed_books:
            print("No books are currently on loan.")
        else:
            print("Books on Loan:")
            for book_id in self.borrowed_books:
                print(f"{book_id}: {self.books[book_id]}")

    def return_book(self):
        try:
            book_id = int(input("Enter the ID of the book to return: "))
            if book_id in self.borrowed_books:
                self.borrowed_books.remove(book_id)
                print(f"Book '{self.books[book_id]}' has been returned.")
            else:
                print("The book is not currently on loan.")
        except ValueError:
            print("Invalid input. Please enter a valid book ID.")

    def list_all_books(self):
        print("Books in Library:")
        for book_id, title in self.books.items():
            print(f"{book_id}: {title}")

    def borrow_book(self):
        try:
            book_id = int(input("Enter the ID of the book to borrow: "))
            if book_id in self.books and book_id not in self.borrowed_books:
                self.borrowed_books.append(book_id)
                print(f"Book '{self.books[book_id]}' has been borrowed.")
            else:
                print("The book is either already borrowed or does not exist.")
        except ValueError:
            print("Invalid input. Please enter a valid book ID.")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1) List all books on loan")
            print("2) Return a book")
            print("3) List all books in the library")
            print("4) Borrow a book")
            print("5) Exit")

            try:
                choice = int(input("Enter choice (1-5): "))
                if choice == 1:
                    self.list_books_on_loan()
                elif choice == 2:
                    self.return_book()
                elif choice == 3:
                    self.list_all_books()
                elif choice == 4:
                    self.borrow_book()
                elif choice == 5:
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Main Function
if __name__ == "__main__":
    system = BookManagementSystem()
    system.menu()
