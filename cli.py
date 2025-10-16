"""
CLI for Bookstore Inventory System (Full CRUD)

Allows users to:
- Add, view, edit, and delete authors, books, and customers
- Record and delete sales
- List books by author or customer
- Export sales and inventory reports (placeholder)

Uses SQLAlchemy ORM to interact with the database.
"""

from db import session
from models.author import Author
from models.book import Book
from models.customer import Customer
from models.sales import Sale
from sqlalchemy import select
from datetime import datetime
# ---------------------- AUTHOR FUNCTIONS ---------------------- #
def add_author():
    """Add a new author to the database."""
    name = input("Enter author name: ").strip()
    nationality = input("Enter nationality (optional): ").strip()
    author = Author(name=name, nationality=nationality)
    session.add(author)
    session.commit()
    print(f"✅ Author added successfully (ID: {author.id})!\n")

def view_authors():
    """List all authors in the system."""
    authors = session.execute(select(Author)).scalars().all()
    if not authors:
        print("No authors found.\n")
        return
    print("\nAuthors:")
    for a in authors:
        print(f"{a.id}: {a.name} ({a.nationality or 'N/A'})")
    print()

def update_author():
    """Edit an existing author's name or nationality."""
    view_authors()
    author_id = int(input("Enter the ID of the author to edit: ").strip())
    author = session.get(Author, author_id)
    if not author:
        print("❌ Author not found.\n")
        return
    new_name = input(f"New name [{author.name}]: ").strip() or author.name
    new_nationality = input(f"New nationality [{author.nationality or 'N/A'}]: ").strip() or author.nationality
    author.name = new_name
    author.nationality = new_nationality
    session.commit()
    print(f"✅ Author '{author.name}' updated successfully!\n")

def delete_author():
    """Remove an author from the database."""
    view_authors()
    author_id = int(input("Enter the ID of the author to delete: ").strip())
    author = session.get(Author, author_id)
    if not author:
        print("❌ Author not found.\n")
        return
    session.delete(author)
    session.commit()
    print(f"✅ Author '{author.name}' deleted successfully!\n")

# ---------------------- BOOK FUNCTIONS ---------------------- #
def add_book():
    """Add a new book to the database and link it to an author."""
    title = input("Enter book title: ").strip()
    price = float(input("Enter price (Ksh): ").strip())
    stock = int(input("Enter stock quantity: ").strip())
    
    authors = session.execute(select(Author)).scalars().all()
    print("\nAvailable authors:")
    for a in authors:
        print(f"{a.id}: {a.name}")
    author_id = int(input("Enter author ID: ").strip())
    
    book = Book(title=title, price=price, stock=stock, author_id=author_id)
    session.add(book)
    session.commit()
    print(f"✅ Book '{title}' added successfully!\n")

def view_books():
    """List all books in the system."""
    books = session.execute(select(Book)).scalars().all()
    if not books:
        print("No books found.\n")
        return
    print("\nBooks:")
    for b in books:
        print(f"{b.id}: {b.title} | Price: {b.price} | Stock: {b.stock} | Author ID: {b.author_id}")
    print()

def update_book():
    """Edit an existing book's details."""
    view_books()
    book_id = int(input("Enter the ID of the book to edit: ").strip())
    book = session.get(Book, book_id)
    if not book:
        print("❌ Book not found.\n")
        return
    new_title = input(f"New title [{book.title}]: ").strip() or book.title
    new_price = input(f"New price [{book.price}]: ").strip()
    new_stock = input(f"New stock [{book.stock}]: ").strip()
    book.title = new_title
    if new_price: book.price = float(new_price)
    if new_stock: book.stock = int(new_stock)
    session.commit()
    print(f"✅ Book '{book.title}' updated successfully!\n")

def delete_book():
    """Remove a book from the database."""
    view_books()
    book_id = int(input("Enter the ID of the book to delete: ").strip())
    book = session.get(Book, book_id)
    if not book:
        print("❌ Book not found.\n")
        return
    session.delete(book)
    session.commit()
    print(f"✅ Book '{book.title}' deleted successfully!\n")

# ---------------------- CUSTOMER FUNCTIONS ---------------------- #
def add_customer():
    """Add a new customer."""
    name = input("Enter customer name: ").strip()
    email = input("Enter email (optional): ").strip()
    customer = Customer(name=name, email=email)
    session.add(customer)
    session.commit()
    print(f"✅ Customer '{name}' added successfully!\n")

def view_customers():
    """List all customers."""
    customers = session.execute(select(Customer)).scalars().all()
    if not customers:
        print("No customers found.\n")
        return
    print("\nCustomers:")
    for c in customers:
        print(f"{c.id}: {c.name} ({c.email or 'N/A'})")
    print()

def update_customer():
    """Edit an existing customer."""
    view_customers()
    customer_id = int(input("Enter the ID of the customer to edit: ").strip())
    customer = session.get(Customer, customer_id)
    if not customer:
        print("❌ Customer not found.\n")
        return
    new_name = input(f"New name [{customer.name}]: ").strip() or customer.name
    new_email = input(f"New email [{customer.email or 'N/A'}]: ").strip() or customer.email
    customer.name = new_name
    customer.email = new_email
    session.commit()
    print(f"✅ Customer '{customer.name}' updated successfully!\n")

def delete_customer():
    """Remove a customer from the database."""
    view_customers()
    customer_id = int(input("Enter the ID of the customer to delete: ").strip())
    customer = session.get(Customer, customer_id)
    if not customer:
        print("❌ Customer not found.\n")
        return
    session.delete(customer)
    session.commit()
    print(f"✅ Customer '{customer.name}' deleted successfully!\n")

# ---------------------- SALES FUNCTIONS ---------------------- #
from datetime import datetime

def record_sale():
    """Record a new sale with quantity and reduce book stock."""
    books = session.execute(select(Book)).scalars().all()
    customers = session.execute(select(Customer)).scalars().all()

    print("\nAvailable Books:")
    for b in books:
        print(f"{b.id}: {b.title} (Stock: {b.stock})")
    print("\nAvailable Customers:")
    for c in customers:
        print(f"{c.id}: {c.name}")

    book_id = int(input("Enter book ID: ").strip())
    customer_id = int(input("Enter customer ID: ").strip())
    quantity = int(input("Enter quantity: ").strip())

    book = session.get(Book, book_id)
    if not book or book.stock < quantity:
        print("❌ Book unavailable or insufficient stock.\n")
        return

    # Use the entered quantity and set date immediately
    sale = Sale(
        book_id=book_id, 
        customer_id=customer_id, 
        quantity=quantity,
        date=datetime.now()  # set date immediately
    )
    book.stock -= quantity
    session.add(sale)
    session.commit()
    print(f"✅ Sale recorded successfully!\n")

def view_sales():
    """List all sales."""
    sales = session.execute(select(Sale)).scalars().all()
    if not sales:
        print("No sales found.\n")
        return
    print("\nSales:")
    for s in sales:
        book = session.get(Book, s.book_id)
        customer = session.get(Customer, s.customer_id)
        print(f"{s.id}: {customer.name} bought '{book.title}' (Qty: {s.quantity}) on {s.date}")
    print()


def delete_sale():
    """Delete a sale and restore book stock based on quantity."""
    view_sales()
    sale_id = int(input("Enter the ID of the sale to delete: ").strip())
    sale = session.get(Sale, sale_id)
    if not sale:
        print("❌ Sale not found.\n")
        return

    # Restore stock based on the quantity sold
    book = session.get(Book, sale.book_id)
    book.stock += sale.quantity

    session.delete(sale)
    session.commit()
    print(f"✅ Sale ID {sale_id} deleted successfully and stock restored!\n")



# ---------------------- LIST FUNCTIONS ---------------------- #
def list_books_by_author():
    author_id = int(input("Enter author ID: ").strip())
    books = session.execute(select(Book).filter_by(author_id=author_id)).scalars().all()
    if not books:
        print("No books found for this author.\n")
        return
    print("\nBooks by this author:")
    for book in books:
        print(f"- {book.title} ({book.stock} in stock)")
    print()

def list_books_by_customer():
    customer_id = int(input("Enter customer ID: ").strip())
    sales = session.execute(select(Sale).filter_by(customer_id=customer_id)).scalars().all()
    if not sales:
        print("No books found for this customer.\n")
        return
    print("\nBooks bought by this customer:")
    for sale in sales:
        book = session.get(Book, sale.book_id)
        print(f"- {book.title}")
    print()

# ---------------------- MAIN CLI ---------------------- #
def main():
    """Main CLI loop."""
    while True:
        print("""
📚 BOOKSTORE INVENTORY SYSTEM 📚
1. Add Author
2. View Authors
3. Edit Author
4. Delete Author
5. Add Book
6. View Books
7. Edit Book
8. Delete Book
9. Add Customer
10. View Customers
11. Edit Customer
12. Delete Customer
13. Record Sale
14. View Sales
15. Delete Sale
16. List Books by Author
17. List Books by Customer
18. Exit
""")
        choice = input("Select an option (1–18): ").strip()

        menu = {
            "1": add_author, "2": view_authors, "3": update_author, "4": delete_author,
            "5": add_book, "6": view_books, "7": update_book, "8": delete_book,
            "9": add_customer, "10": view_customers, "11": update_customer, "12": delete_customer,
            "13": record_sale, "14": view_sales, "15": delete_sale,
            "16": list_books_by_author, "17": list_books_by_customer
        }

        if choice in menu:
            menu[choice]()
        elif choice == "18":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
