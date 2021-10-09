# EJERCICIO 1

palabra = input("Introduce una palabra: ")
for i in range(10):
    print(palabra)

# EJERCICIO 2

edad = int(input("¿Cuántos años tienes? "))
for i in range(edad):
    print("Has cumplido " + str(i+1) + " años")

# EJERCICIO 3

n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")

# EJERCICIO 4

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

# EJERCICIO 5

key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")

# EJERCICIO 6

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)