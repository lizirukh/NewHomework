class Book():
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year


# books_list = []
#
# class BookManager():
#     def add_new_book(self, name, author, year):
#         new_book = Book(self.name, self.author, self.year)
#         books_list.append(new_book)
#
#     def display_books(self):
#         for book in books_list:
#             print(f'{self.book.name} - {self.book.author} - {self.book.year}')
#
#     def search_book(self, name):
#         for book in books_list:
#             if book.name == name:
#                 print(f'{self.book.name} - {self.book.author} - was issued in {self.book.year}')



# def user_interface(user_input):
#     if user_input == 1:
#         name = input("Please enter the name of the book:")
#         author = input("Please enter the name of the author:")
#         year = int(input("Please enter the year the book was issued:"))
#         BookManager.add_new_book(name, author, year)
#     if user_input == 2:
#         BookManager.display_books()
#     if user_input == 3:
#         name = input("Please enter the name of the book:")
#         BookManager.search_book(name)

book1 = Book("Animal Farm", "George Orwell", 1985)
print(book1)

# books_list.append(books)
# BookManager.display_books()

# usr_input = int(input(f"Please, enter number according to the action you would like to take: \n1 if you would like to add a new book \n2 if you would like to see the list of the books \n3 if you would like to search the book by it's name \n Type Here: "))

# user_interface(usr_input)
