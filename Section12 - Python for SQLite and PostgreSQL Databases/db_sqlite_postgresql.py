import sqlite3

def create_table():
    # Connect to/create database
    conn = sqlite3.connect("lite.db")
    # create curson object
    cur = conn.cursor()
    # create table
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # commit changes to db
    conn.commit()
    # close connection to db
    conn.close()

def insert():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # add data to table
    cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
    conn.commit()
    conn.close()