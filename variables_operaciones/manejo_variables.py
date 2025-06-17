a = 10
b = 3

# Operaciones
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

# Comparaciones
x = 5
y = 10
print("x == y:", x == y)
print("x != y:", x != y)

# Lógicas
print("AND:", True and False)
print("OR:", True or False)
print("NOT:", not True)

# Strings
texto = "Hola, Python"
print(texto.upper())
print(texto.lower())
print(len(texto))
print(texto.replace("Python", "Mundo"))

# Listas
lista = [1, 2, 3]
lista.append(4)
lista.remove(2)
lista.sort()
print(lista)

# Diccionarios
diccionario = {"nombre": "Ana", "edad": 25}
diccionario["ciudad"] = "Bogotá"
del diccionario["edad"]
print(diccionario)

# Conversiones
numero = 10
print(str(numero))
print(list("Hola"))
print(float("3.14"))
