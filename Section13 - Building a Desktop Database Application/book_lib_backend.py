"""
The backend script for the book library frontend

"""

import sqlite3

# Create a db / connection to db
def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book"
        "("
            "id INTEGER PRIMARY KEY"
            ", title TEXT"
            ", author TEXT"
            ", year INTEGER"
            ", isbn INTEGER"
        ")"
    )
    conn.commit()
    conn.close()

# Insert data into db
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
    #conn.commit()
    rows = cur.fetchall()
    return rows

connect()
insert("Test 1", "Book Worm", 1918, 1234567890)
print(view())
print(search(author="Book Worm"))