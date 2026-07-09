from database.session import engine
from sqlmodel import SQLModel
from models.book import Book
from models.category import Category

# Drop all tables
SQLModel.metadata.drop_all(engine)
print("Tables dropped successfully")
