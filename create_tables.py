print("▶ Starting table creation...")
from db import Base, engine
from models.author import Author
from models.book import Book
from models.customer import Customer
from models.sales import Sale

print("Creating database tables...")
Base.metadata.create_all(engine)
print("✅ Tables created successfully!")
