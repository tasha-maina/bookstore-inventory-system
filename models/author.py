from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    nationality = Column(String, nullable=True)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(id={self.id}, name={self.name})>"
