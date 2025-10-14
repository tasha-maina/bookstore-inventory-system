from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    # Relationship to Author
    author = relationship("Author", back_populates="books")

    # Relationship to Sales
    sales = relationship("Sale", back_populates="book")
