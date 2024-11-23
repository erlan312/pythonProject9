import sqlite3
from dbm import error


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connection(db_name)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_CONECTION')
    return connection

def create_table(connection,sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_TABLE function')

def insert_products(connection,product):
    try:
        sql = '''INSERT INTO products 
        
        (roduct_title,price,quantity)
        VALUES (?,?,?)'''
        cursor = connection.cursor()
        cursor.execute(sql,product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in INSERT_PRODUCTS function')


def Update_quantuty(connection, product):
    try:
        sql = '''UPDATE products SET price=? WHERE id=? '''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_QUANTITY function')


def Update_price(connection, product):
    try:
        sql = '''UPDATE products SET price=? WHERE id=? '''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_PRICE function')


def delete_by_id(connection, id):
    try:
        sql = ''' DELETE FROM products WHERE id=? '''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in DELETE_BY_ID function')


def seleckt_all(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELLECT_ALL function')

def seleckt_by_price_and_quantity(connection, limit):
    try:
        sql = '''SELECT * FROM products
        WHERE price <=? AND quantity >=?'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELLECT_BY_PRICE_AND_QUANTITY function')

def seleckt_by_name(connection):
    try:
        sql = '''SELECT * FROM products
        WHERE product_title LIKE "%kurut%"
        '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELLECT_BY_NAME function')


sql_to_create_products_title = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT (10,2) NOT NULL DEFOULT 0.0,
    quantity INTIGER NOT NULL DEFOULT 0
)
'''


my_connection = create_connection(hw.db)

if my_connection:
    print ('Connected successfully!')

    create_table(my_connection, sql_to_create_products_table)
    insert_products(my_connection, ('Classic Chocolate',120.50, 7))
    insert_products(my_connection, ('Milk Chocolate', 129.99, 3))
    insert_products(my_connection, ('White Chocolate', 99.99, 10))
    insert_products(my_connection, ('Black chocolate', 150.40, 8))
    insert_products(my_connection, ('Salted Chocolate', 145.50, 5))
    insert_products(my_connection, ('Classic Marmalade',89.90, 12))
    insert_products(my_connection, ('Berry Marmalade', 100.00,10))
    insert_products(my_connection, ('Fruit Marmalade', 100.00, 7))
    insert_products(my_connection, ('Classic Kurut',   30.30, 15))
    insert_products(my_connection, ('Smoked Kurut', 35.50, 4))
    insert_products(my_connection, ('Mint Gum', 45.80, 9))
    insert_products(my_connection, ('Fruit Gum', 43.30, 3))
    insert_products(my_connection,  ('Cheese Chips', 150.70, 4))
    insert_products(my_connection, ('Spicy Chips', 145.99, 7))
    insert_products(my_connection, ("salted chips", 120.00, 2))
