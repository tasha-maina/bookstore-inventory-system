from models.sales import Sale
from models.book import Book
from models.customer import Customer

def test_sale_creation():
    book = Book(title="Sale Book", price=15.0, stock=10)
    cust = Customer(name="Bob", email="bob@example.com")
    sale = Sale(book=book, customer=cust, quantity=2)
    assert sale.quantity == 2
    assert sale.book is book
    assert sale.customer is cust
