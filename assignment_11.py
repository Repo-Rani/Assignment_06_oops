# 11. Class Methods

class Book:
    total_books: int = 0

    def __init__(self):
        Book.increment_book_count()  

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

book1 = Book()
book2 = Book()

print(f"Total Books: {Book.get_total_books()}")