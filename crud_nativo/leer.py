from conexion import conectar

def leer():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas")
    for fila in cursor.fetchall():
        print(fila)
    conn.close()