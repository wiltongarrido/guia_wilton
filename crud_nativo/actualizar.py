from conexion import conectar

def actualizar(id, nombre, apellido, edad, correo, numero):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE personas SET nombre=?, apellido=?, edad=?, correo=?, numero=? WHERE id=?",
                   (nombre, apellido, edad, correo, numero, id))
    conn.commit()
    conn.close()
    print("Registro actualizado correctamente.")