class Book():
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year


class BookManager():
    def __init__(self):
        self.books_lst = []

    def add_new_book(self, book):
        if isinstance(book, Book):
            self.books_lst.append(book)
            return f'Book {book.name} added successfully.'
        return 'Invalid book type'

    def display_books(self):
            if not self.books_lst:
                return 'The list is empty.'
            return "\n".join([
            f'{index + 1}. "{book.name}" by {book.author} ({book.year})'
            for index, book in enumerate(self.books_lst)
        ])


    def search_book(self, name):
        matches = [book for book in self.books_lst if book.name == name]
        if not matches:
            return f'No book found with the name "{name}".'
        for book in matches:
            return f'{book.name} by {book.author} ({book.year})'


def user_interface():
    manager = BookManager()

    while True:
        print("\nWelcome to the Book Manager!")
        print("1. Add a new book")
        print("2. Display the list of books")
        print("3. Search for a book by name")
        print("4. Exit")

        try:
            usr_input = int(input("Enter your choice (1-4): "))

            if usr_input == 1:
                name = input("Enter the name of the book: ")
                author = input("Enter the author of the book: ")
                year = input("Enter the year of issue: ")

                if not year.isdigit():
                    print("Year must be a valid number. Please, try again!")
                else:
                    book = Book(name, author, int(year))
                    print(manager.add_new_book(book))

            elif usr_input == 2:
                print('\nList of Books:')
                print(manager.display_books())

            elif usr_input == 3:
                search_name = input("Enter the name of the book: ")
                print('\nSearch Result:')
                print(manager.search_book(search_name))

            elif usr_input == 4:
                print('Exiting the application!')
                break

            else:
                print('Invalid input! Please, enter number between 1-4 ')

        except ValueError:
            print("Invalid input. Please enter a valid number.")

user_interface()

