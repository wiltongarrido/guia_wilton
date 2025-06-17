from conexion import conectar

def crear(nombre, apellido, edad, correo, numero):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO personas (nombre, apellido, edad, correo, numero) VALUES (?, ?, ?, ?, ?)",
                   (nombre, apellido, edad, correo, numero))
    conn.commit()
    conn.close()
    print("Registro creado correctamente.")