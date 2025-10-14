from db import session
from models.author import Author
from models.book import Book
from models.customer import Customer
from models.sales import Sale
from sqlalchemy import select
from datetime import datetime

def add_author():
    name = input("Enter author name: ").strip()
    nationality = input("Enter nationality (optional): ").strip()
    author = Author(name=name, nationality=nationality)
    session.add(author)
    session.commit()
    print(f"✅ Author added successfully (ID: {author.id})!\n")

def add_book():
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

def add_customer():
    name = input("Enter customer name: ").strip()
    email = input("Enter email (optional): ").strip()
    customer = Customer(name=name, email=email)
    session.add(customer)
    session.commit()
    print(f"✅ Customer '{name}' added successfully!\n")

def record_sale():
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

    book = session.get(Book, book_id)
    if not book or book.stock <= 0:
        print("❌ Book unavailable or out of stock.\n")
        return

    sale = Sale(book_id=book_id, customer_id=customer_id)
    book.stock -= 1  # reduce stock
    session.add(sale)
    session.commit()
    print(f"✅ Sale recorded successfully!\n")

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

def main():
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
8. Export inventort report
9. Exit
""")
        choice = input("Select an option (1–7): ").strip()

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
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
