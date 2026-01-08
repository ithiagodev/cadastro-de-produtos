import sqlite3

def create_table():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS products ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL CHECK (price >= 0),
                    stock INTEGER NOT NULL CHECK (stock >= 0))''')
    
    connection.commit()
    connection.close()

def create_product(name, description, price, stock):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?) ''', (name, description, price, stock))

    product_id = cursor.lastrowid
    connection.commit()
    connection.close()

    return product_id

def get_product(product_id=None):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    if product_id is None:
        cursor.execute('SELECT * FROM products')
        product = cursor.fetchall()
        connection.close()
        return product

    else:
        cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        product = cursor.fetchone()
        connection.close()
        return product

def update_product(product_id, name=None, description=None, price=None, stock=None):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)

    if description is not None:
        fields.append("description = ?")
        values.append(description)

    if price is not None:
        fields.append("price = ?")
        values.append(price)

    if stock is not None:
        fields.append("stock = ?")
        values.append(stock)

    if not fields:
        connection.close()
        return

    query = f"UPDATE products SET {', '.join(fields)} WHERE id = ?"
    values.append(product_id)

    cursor.execute(query, values)
    connection.commit()
    connection.close()

def delete_product(product_id):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    if cursor.rowcount == 0:
        connection.close()
        return False

    connection.commit()
    connection.close()
    return True