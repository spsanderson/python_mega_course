"""
The backend script for the book library frontend.

connect(), insert(), delete(), search(), update(), view()

"""

import sqlite3

class Database:

    # Create a db / connection to db
    def __init__(self, db):
        conn = sqlite3.connect(db)
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
    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        conn.commit()
        conn.close()
    # View data
    def view(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        conn.commit()
        rows = cur.fetchall()
        conn.close()
        return rows
    # Search data
    def search(self, title="", author="", year="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
        conn.commit()
        rows = cur.fetchall()
        conn.close()
        return rows
    # Delete record
    def delete(self, id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()
    # Update record
    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
        conn.commit()
        conn.close()
