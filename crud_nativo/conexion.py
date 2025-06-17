import sqlite3

def conectar():
    conn = sqlite3.connect('personas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        edad INTEGER,
        correo TEXT,
        numero TEXT
    )''')
    conn.commit()
    return conn