# 📚 Bookstore Inventory System (CLI + ORM Project)

## 🧾 Overview
A command-line application built in Python that manages a bookstore's authors, books, customers, and sales using **SQLAlchemy ORM** and **PostgreSQL**.

### 🎯 Features
- Add, view, and manage **Authors**, **Books**, and **Customers**
- Record book sales with stock tracking
- Generate **CSV sales reports**
- Calculate **total sales per author**
- Uses PostgreSQL with SQLAlchemy ORM
- Clean CLI interface


## 🏗️ Database Schema

**Relationships:**
- One **Author** → Many **Books**
- One **Book** → Many **Customers** (through `sales`)
- One **Customer** → Many **Books** (through `sales`)

Tables:
1. `authors`
2. `books`
3. `customers`
4. `sales` (join table with timestamp)


## 🧰 Technologies Used
- Python 3
- SQLAlchemy ORM
- PostgreSQL (via psycopg2)
- Beekeeper Studio (for DB visualization)
- Pipenv (for environment management)


## ⚙️ Setup Instructions

1. **Clone the repo**

   git clone https://github.com/tasha-maina/bookstore_inventory_system.git
   cd bookstore_inventory_system
Create the virtual environment

pipenv install
pipenv shell


Set up your .env

DATABASE_USER=postgres
DATABASE_PASSWORD=my_postgres_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=bookstore_db


Create tables

python create_tables.py


Run the CLI

python cli.py

🧪 Example Flow

Add Author → “Chimamanda Adichie”

Add Book → “Purple Hibiscus” linked to Author ID 1

Add Customer → “Natasha Banks”

Record Sale → Natasha buys Purple Hibiscus

Export CSV → Generates sales_report_YYYYMMDD.csv

Check your Beekeeper → All tables populated 🎉

📊 Example CLI Output
=== Bookstore Inventory System ===
1. Add Author
2. Add Book
3. Add Customer
4. Record Sale
5. List Books by Author
6. List Books by Customer
7. Export Sales CSV
8. Show Total Sales per Author
9. Exit

👩‍💻 Author

Created by Natasha Banks