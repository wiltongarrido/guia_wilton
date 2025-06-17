from conexion import conectar

def eliminar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM personas WHERE id=?", (id,))
    conn.commit()
    conn.close()
    print("Registro eliminado correctamente.")