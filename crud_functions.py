import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        );
        ''')
    cursor.execute("CREATE INDEX IF NOT EXISTS title ON Products (title)")
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute(" SELECT id, title, description, price FROM Products")
    items = cursor.fetchall()
    connection.commit()
    connection.close()
    return items


def item_add(item_list):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Products (title, description, price) VALUES(?, ?, ?);", item_list)
    connection.commit()
    connection.close()
