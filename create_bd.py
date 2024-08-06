import sqlite3
import add_items




connection = sqlite3.connect('catalog_of_goods.db')
cursor = connection.cursor()


def create_bd():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Catalog(
    id INTEGER PRIMARY KEY,
    part_number INTEGER NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_part_number ON Catalog (part_number)")


def item_add(item_list):
    cursor.executemany("INSERT INTO Catalog (part_number, description, price) VALUES(?, ?, ?);", item_list)


create_bd()
item_add(add_items.part_list)

connection.commit()
connection.close()
