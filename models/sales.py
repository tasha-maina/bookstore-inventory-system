from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from db import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    date = Column(DateTime, server_default=func.now())

    # Relationships
    book = relationship("Book", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
