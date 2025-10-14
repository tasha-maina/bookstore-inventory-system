import csv
from db import session
from models.book import Book
from models.author import Author
from models.sales import Sale
from models.customer import Customer
from sqlalchemy import select
from datetime import datetime

def export_sales_report():
    filename = f"sales_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Sale ID", "Book Title", "Customer", "Date"])
        sales = session.execute(select(Sale)).scalars().all()
        for sale in sales:
            book = session.get(Book, sale.book_id)
            customer = session.get(Customer, sale.customer_id)
            writer.writerow([sale.id, book.title, customer.name, sale.date])
    print(f"✅ Sales report exported successfully: {filename}\n")

def export_inventory_report():
    filename = f"inventory_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Book Title", "Author", "Price (Ksh)", "Stock"])
        books = session.execute(select(Book)).scalars().all()
        for book in books:
            author = session.get(Author, book.author_id)
            writer.writerow([book.title, author.name, book.price, book.stock])
    print(f"✅ Inventory report exported successfully: {filename}\n")
