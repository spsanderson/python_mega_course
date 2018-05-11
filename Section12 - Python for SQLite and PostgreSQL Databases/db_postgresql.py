import psycopg2
conn_str = "dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'"

def create_table():
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

create_table()

def insert(item, quantity, price):
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    # add data to table
    # The below is prone to SQL injection
    #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price))
    # Passing items as second parameter will help solve the above
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()

insert("Water Glass", 10, 5.5)
insert("Coffee",5,5)
insert("Wine Glass",10,7)

def view():
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s",(item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    cur.execute(
        "UPDATE store SET quantity = %s, price = %s WHERE item = %s"
        , (quantity, price, item))
    conn.commit()
    conn.close()

delete("Wine Glass")
update(10, 11, "Water Glass")
print(view())
