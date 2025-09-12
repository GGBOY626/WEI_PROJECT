import os
import sqlite3
import threading
import time

DB_PATH = "app.db"


if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, item TEXT)")

for uid in range(1, 11):
    cur.execute("INSERT INTO users (id, name) VALUES (?, ?)", (uid, f"user_{uid}"))
    for j in range(5):
        cur.execute("INSERT INTO orders (user_id, item) VALUES (?, ?)", (uid, f"item_{j}"))
conn.commit()
conn.close()
class Database:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls, db_name = "app.db"):
        if not cls._instance: # first check
            with cls._lock: # Lock
                if not cls._instance: # double check to protect single instance
                    cls._instance = super(Database,cls).__new__(cls)
                    cls._instance.conn = sqlite3.connect(db_name,check_same_thread=False)
                    cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance
    def get_cursor(self):
        return self.cursor
    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
        Database._instance = None
class UserService:
    def get_user(self, user_id):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        return result


class OrderService:
    def get_orders(self, user_id):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        return result

class BaselineUserService:
    def get_user(self, user_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result

class BaselineOrderService:
    def get_orders(self, user_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result


def bench(user_service, order_service, loops=2000):
    start = time.perf_counter()
    for i in range(loops):
        uid = (i % 10) + 1
        user_service.get_user(uid)
        order_service.get_orders(uid)
    return time.perf_counter() - start


if __name__ == "__main__":
    loops = 2000
    #original
    t1 = bench(BaselineUserService(), BaselineOrderService(), loops)

    # single
    UserService().get_user(1)
    t2 = bench(UserService(), OrderService(), loops)
    Database().close()

    print(f"original time: {t1:.4f} second")
    print(f"single time: {t2:.4f} second")