import sqlite3


def initiate_db():
    '''
    Создание базы продуктов с индексацией по колонке title
    :return:
    '''
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


def initiate_db_user():
    '''
    Создание базы пользователей, индексация по колонке username
    :return:
    '''
    connect = sqlite3.connect('users.db')
    cur = connect.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        );
        ''')
    cur.execute("CREATE INDEX IF NOT EXISTS username ON Users (username)")
    connect.commit()
    connect.close()


def get_all_products():
    '''
    Запрос полного списка продуктов
    :return: список кортежей продуктов
    '''
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute(" SELECT id, title, description, price FROM Products")
    items = cursor.fetchall()
    connection.commit()
    connection.close()
    return items


def item_add(item_list):
    '''
    Добавляет список продуктов в базу
    :param item_list:
    :return: None
    '''
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Products (title, description, price) VALUES(?, ?, ?);", item_list)
    connection.commit()
    connection.close()


def add_user(username, email, age):
    '''
    Принимает: имя пользователя, почту и возраст.
    Данная функция должна добавлять в таблицу Users
    :param username:
    :param email:
    :param age:
    :return:
    '''
    connect = sqlite3.connect('users.db')
    cur = connect.cursor()
    cur.execute(f'''
    INSERT INTO Users(username, email, age, balance) VALUES('{username}', '{email}', '{age}', 1000);
    ''')
    connect.commit()
    connect.close()


def is_included(username):
    '''
    Принимает имя пользователя и возвращает True,
    если такой пользователь есть в таблице Users,
    в противном случае False.
    :param username:
    :return:
    '''
    connect = sqlite3.connect('users.db')
    cur = connect.cursor()
    check_user = cur.execute("SELECT * FROM Users WHERE username =? ", (username,))
    if check_user.fetchone() is None:
        connect.commit()
        connect.close()
        return False
    else:
        connect.commit()
        connect.close()
        return True
