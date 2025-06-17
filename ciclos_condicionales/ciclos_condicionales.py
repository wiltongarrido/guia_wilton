for i in range(3):
    print("For:", i)

x = 0
while x < 3:
    print("While:", x)
    x += 1

num = 10
if num > 0:
    print("Positivo")
elif num == 0:
    print("Cero")
else:
    print("Negativo")

for i in range(5):
    if i == 3:
        break
    print("Break:", i)

for i in range(5):
    if i == 2:
        continue
    print("Continue:", i)
