from database import get_db

def add_expense(title, amount, category):
    conn = get_db()
    conn.execute("INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",
                 (title, amount, category))
    conn.commit()
    conn.close()

def get_all_expenses():
    conn = get_db()
    rows = conn.execute("SELECT * FROM expenses").fetchall()
    conn.close()
    return rows
