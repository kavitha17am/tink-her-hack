import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Create books table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL
    )
""")

# Sample book data
books = [
    ("To Kill a Mockingbird", "Harper Lee", "Fiction"),
    ("1984", "George Orwell", "Fiction"),
    ("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
    ("Dune", "Frank Herbert", "Science Fiction"),
    ("Neuromancer", "William Gibson", "Science Fiction"),
    ("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"),
    ("Dracula", "Bram Stoker", "Horror"),
    ("The Turn of the Screw", "Henry James", "Horror"),
    ("The Girl Next Door", "Jack Ketchum", "Horror"),
    ("A Midsummer Night's Dream", "William Shakespeare", "Rom-Com"),
    ("Pride and Prejudice", "Jane Austen", "Rom-Com"),
]

# Insert books only if they don't already exist
for book in books:
    cursor.execute("""
        INSERT INTO books (title, author, genre)
        SELECT ?, ?, ?
        WHERE NOT EXISTS (
            SELECT 1 FROM books WHERE title=? AND author=? AND genre=?
        )
    """, (book[0], book[1], book[2]))

# Commit and close the connection
conn.commit()
conn.close()
print("Database setup complete! No duplicate books added.")