"""
CLI for Bookstore Inventory System

This application allows users to:
- Add and view authors, books, and customers
- Record sales
- List books by author or customer
- Export sales and inventory reports

Uses SQLAlchemy ORM to interact with the database.
"""

from db import session
from models.author import Author
from models.book import Book
from models.customer import Customer
from models.sales import Sale
from sqlalchemy import select
from datetime import datetime

def add_author() -> None:
    """
    Prompt the user to add a new author.

    Collects the author's name and optional nationality.
    Saves the author to the database.
    """
    name = input("Enter author name: ").strip()
    nationality = input("Enter nationality (optional): ").strip()
    
    author = Author(name=name, nationality=nationality)
    session.add(author)
    session.commit()
    
    print(f"✅ Author added successfully! ID: {author.id}\n")


def add_book() -> None:
    """
    Prompt the user to add a new book.

    Collects title, price, stock quantity, and author selection.
    Saves the book to the database and links it to the chosen author.
    """
    title = input("Enter book title: ").strip()
    
    # Validate price input
    while True:
        try:
            price = float(input("Enter price (Ksh): ").strip())
            break
        except ValueError:
            print("❌ Please enter a valid number for the price.")
    
    # Validate stock input
    while True:
        try:
            stock = int(input("Enter stock quantity: ").strip())
            break
        except ValueError:
            print("❌ Please enter a valid number for stock.")

    # Display authors for selection
    authors = session.execute(select(Author)).scalars().all()
    print("\nAvailable authors:")
    for a in authors:
        print(f"{a.id}: {a.name}")
    
    while True:
        try:
            author_id = int(input("Enter author ID: ").strip())
            if any(a.id == author_id for a in authors):
                break
            else:
                print("❌ Author ID not found. Try again.")
        except ValueError:
            print("❌ Please enter a valid number.")

    book = Book(title=title, price=price, stock=stock, author_id=author_id)
    session.add(book)
    session.commit()
    print(f"✅ Book '{title}' added successfully!\n")


def add_customer() -> None:
    """
    Prompt the user to add a new customer.

    Collects customer name and optional email.
    Saves the customer to the database.
    """
    name = input("Enter customer name: ").strip()
    email = input("Enter email (optional): ").strip()
    
    customer = Customer(name=name, email=email)
    session.add(customer)
    session.commit()
    
    print(f"✅ Customer '{name}' added successfully!\n")


def record_sale() -> None:
    """
    Record a sale in the system.

    Displays available books and customers.
    Reduces book stock by 1 when a sale is recorded.
    Saves the sale to the database.
    """
    books = session.execute(select(Book)).scalars().all()
    customers = session.execute(select(Customer)).scalars().all()

    if not books:
        print("❌ No books available.\n")
        return
    if not customers:
        print("❌ No customers available.\n")
        return

    print("\nAvailable Books:")
    for b in books:
        print(f"{b.id}: {b.title} (Stock: {b.stock})")

    print("\nAvailable Customers:")
    for c in customers:
        print(f"{c.id}: {c.name}")

    while True:
        try:
            book_id = int(input("Enter book ID: ").strip())
            book = session.get(Book, book_id)
            if book and book.stock > 0:
                break
            else:
                print("❌ Book unavailable or out of stock. Choose another.")
        except ValueError:
            print("❌ Please enter a valid number.")

    while True:
        try:
            customer_id = int(input("Enter customer ID: ").strip())
            customer = session.get(Customer, customer_id)
            if customer:
                break
            else:
                print("❌ Customer ID not found.")
        except ValueError:
            print("❌ Please enter a valid number.")

    sale = Sale(book_id=book_id, customer_id=customer_id, quantity=1)
    book.stock -= 1
    session.add(sale)
    session.commit()

    print(f"✅ Sale recorded: 1 x '{book.title}' sold to {customer.name}!\n")


def list_books_by_author() -> None:
    """
    List all books by a specific author.

    Prompts for author ID and fetches associated books.
    Displays book title and stock.
    """
    while True:
        try:
            author_id = int(input("Enter author ID: ").strip())
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    books = session.execute(select(Book).filter_by(author_id=author_id)).scalars().all()
    if not books:
        print("No books found for this author.\n")
        return

    print("\nBooks by this author:")
    for book in books:
        print(f"- {book.title} ({book.stock} in stock)")
    print()


def list_books_by_customer() -> None:
    """
    List all books purchased by a specific customer.

    Prompts for customer ID and fetches associated sales.
    Displays book titles for each sale.
    """
    while True:
        try:
            customer_id = int(input("Enter customer ID: ").strip())
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    sales = session.execute(select(Sale).filter_by(customer_id=customer_id)).scalars().all()
    if not sales:
        print("No books found for this customer.\n")
        return

    print("\nBooks bought by this customer:")
    for sale in sales:
        book = session.get(Book, sale.book_id)
        print(f"- {book.title}")
    print()


def main() -> None:
    """
    Main CLI loop.

    Displays the menu and executes functions based on user selection.
    Loops until user exits.
    """
    while True:
        print("""
📚 BOOKSTORE INVENTORY SYSTEM 📚
1. Add new author
2. Add new book
3. Add new customer
4. Record a sale
5. List all books by author
6. List all books bought by customer
7. Export sales report
8. Export inventory report
9. Exit
""")
        choice = input("Select an option (1–9): ").strip()

        if choice == "1":
            add_author()
        elif choice == "2":
            add_book()
        elif choice == "3":
            add_customer()
        elif choice == "4":
            record_sale()
        elif choice == "5":
            list_books_by_author()
        elif choice == "6":
            list_books_by_customer()
        elif choice in ["7", "8"]:
            print("⚠️ Report exporting not implemented yet.\n")
        elif choice == "9":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
