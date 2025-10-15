from models.book import Book
from models.author import Author

def test_book_creation_without_author():
    book = Book(title="My Book", price=12.99, stock=5)
    assert book.title == "My Book"
    assert book.price == 12.99
    assert book.stock == 5

def test_book_author_relationship():
    author = Author(name="John Smith", nationality="Ugandan")
    book = Book(title="Another Book", price=20.0, stock=3, author=author)
    assert book.author is author
    assert book.author.name == "John Smith"
