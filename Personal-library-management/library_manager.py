import json
class BookCollection:
    def __init__(self):
        self.books = []
        self.file = "books.json"
        self.read_books()

    def read_books(self):
        try:
            with open(self.file, "r") as file:
                self.books = json.load(file) 
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        with open(self.file, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = input("Enter the publication year: ")
        genre = input("Enter the genre: ")
        read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        self.books.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
        self.save_books()
        print("✅  Book added successfully! \n")

    def remove_book(self):
        book_title = input("Enter the title of the book to remove: ").strip().lower()
        for book in self.books:
            if book["title"].lower() == book_title:
                self.books.remove(book)
                self.save_books()
                print("✅  Book removed successfully!\n")
                return
        print("⚠️  Book not found!\n")

    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search by:\n1. Title \n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.books  # Fix: Use self.books instead of self.book_list
            if search_text in book["title"].lower() or search_text in book["author"].lower()
        ]

        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        else:
            print("⚠️  No matching books found.\n")

    def display_books(self):
        if not self.books:
            print("No books in collection.\n")
        else:
            for book in self.books:
                print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        print()

    def show_progress(self):
        total = len(self.books)
        read_count = sum(b["read"] for b in self.books)
        print(f"Total: {total}, Read: {read_count}, Read %: {read_count/total*100 if total else 0:.2f}%\n")

    def menu(self):
        while True:
            print("📚 Welcome to your Personal Library Manager! ✨ ")
            print("1. Add Book  2. Remove Book  3. Search  4. Display  5. Progress  6. Exit")
            choice = input("Select any one from the above: ").strip()
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.find_book()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.show_progress()
            elif choice == "6":
                self.save_books()
                print("Library saved to file. Goodbye! ")
                break
            else:
                print("📌 Invalid choice!\n")

if __name__ == "__main__":
    BookCollection().menu()
print(" 🚀 Created by KASHAF AMAN")