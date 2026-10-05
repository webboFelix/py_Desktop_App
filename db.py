import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, parts text, customer text, retailer text, price text)"
        )
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, parts, customer, retailer, price):
        self.cur.execute(
            "INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)", (parts, customer, retailer, price)
        )
        self.conn.commit()
        
    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()
        
    def update(self, id, parts, customer, retailer, price):
        self.cur.execute(
            "UPDATE parts SET parts = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
            (parts, customer, retailer, price, id),
        )
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
    
db = Database("store.db")

# db.insert("iPhone 12", "John Doe", "Apple Store", "$799")
# db.insert("Samsung Galaxy S21", "Jane Smith", "Samsung Store", "$999")
# db.insert("Google Pixel 6", "Bob Johnson", "Google Store", "$699")
# db.insert("OnePlus 1", "Ali Brown", "OnePlus Store", "$729")
# db.insert("OnePlus 4", "Alice Brown", "OnePlus Store", "$573")
# db.insert("OnePlus 7", "Alice Byron", "OnePlus Store", "$886")
# db.insert("OnePlus 9", "Otile Brown", "OnePlus Store", "$893")
