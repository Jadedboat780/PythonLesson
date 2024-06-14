# Приложение ИНТЕРНЕТ-МАГАЗИН для некоторой организации.
# БД должна содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
# единицу измерения (штуки, килограммы, литры), количество, стоимость.

import sqlite3


class DataBase:
    def __init__(self, db_url: str):
        self.conn = sqlite3.connect(db_url)

    def create_database(self):
        cursor = self.conn.cursor()
        query = '''
        CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name VARCHAR(150) NOT NULL,
                product VARCHAR(50) NOT NULL,
                unit VARCHAR(50) NOT NULL,
                quantity INT NOT NULL CHECK ( quantity >= 0 ),
                cost INT CHECK ( cost > 0 )
                )
                '''

        cursor.execute(query)
        self.conn.commit()

    def add_sale(self, customer_name, product, unit, quantity, cost):
        cursor = self.conn.cursor()
        query = '''
        INSERT INTO sales (customer_name, product, unit, quantity, cost)
        VALUES (?, ?, ?, ?, ?)
        '''
        cursor.execute(query, (customer_name, product, unit, quantity, cost))

        self.conn.commit()

    def update_sale(self, sale_id, customer_name=None, product=None, unit=None, quantity=None, cost=None):
        cursor = self.conn.cursor()
        fields = {
            "customer_name": customer_name,
            "product": product,
            "unit": unit,
            "quantity": quantity,
            "cost": cost
        }
        updates = ", ".join([f"{key} = ?" for key, value in fields.items() if value is not None])
        values = [value for value in fields.values() if value is not None]
        query = f"UPDATE sales SET {updates} WHERE id = ?"
        cursor.execute(query, (*values, sale_id))
        self.conn.commit()

    def delete_sale(self, sale_id):
        cursor = self.conn.cursor()
        query = "DELETE FROM sales WHERE id = ?"
        cursor.execute(query, (sale_id,))
        self.conn.commit()

    def get_sales(self):
        cursor = self.conn.cursor()
        query = 'SELECT * FROM sales'
        cursor.execute(query)
        sales = cursor.fetchall()
        return sales

    def __del__(self):
        self.conn.close()


db = DataBase("product.db")
db.create_database()
db.add_sale("Tokin Nikita 1", "Games 1", "кг", 15, 1500)
db.add_sale("Tokin Nikita 2", "Games 2", "г", 50, 150)
db.add_sale("Tokin Nikita 3", "Games 3", "м", 150, 300)
db.update_sale(2, customer_name="K")
db.delete_sale(3)
print(db.get_sales())