from crear import crear
from leer import leer
from actualizar import actualizar
from eliminar import eliminar

while True:
    print("\n1. Crear\n2. Leer\n3. Actualizar\n4. Eliminar\n5. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        correo = input("Correo: ")
        numero = input("Número: ")
        crear(nombre, apellido, edad, correo, numero)
    elif opcion == "2":
        leer()
    elif opcion == "3":
        id = int(input("ID a actualizar: "))
        nombre = input("Nuevo nombre: ")
        apellido = input("Nuevo apellido: ")
        edad = int(input("Nueva edad: "))
        correo = input("Nuevo correo: ")
        numero = input("Nuevo número: ")
        actualizar(id, nombre, apellido, edad, correo, numero)
    elif opcion == "4":
        id = int(input("ID a eliminar: "))
        eliminar(id)
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")