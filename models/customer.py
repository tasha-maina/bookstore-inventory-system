from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)

    # Relationship to Sales
    sales = relationship("Sale", back_populates="customer")
