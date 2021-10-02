# # ***** OPERADORES DE COMPARACION *****
# numero = int(input("Escriba un numero del 1 al 10:"))
# if numero > 10:
#     print("¡El numero que has escrito es mayor que 10!")
# print("Has escrito el numero " + str(numero))

# cadenaejemplo = "En un lugar de Buenos Aires..."
# if "lugar" in cadenaejemplo:
#     print("encontrado")
# else:
#     print("no encontrado")

# cadenaejemplo = "En un lugar de Buenos Aires..."
# if cadenaejemplo.startswith('E'):
#     print("empieza por E")
# else:
#     print("no empieza por E")
# if cadenaejemplo.endswith('.'):
#     print("termina por .")
# else:
#     print("no termina por .")

numero1 = int(input("Escriba el primer numero:"))
numero2 = int(input("Escriba el segundo numero:"))
if numero1>numero2:
    print("el primer numero es mayor que el segundo")
elif numero1==numero2:
    print("Ambos numeros son iguales")
else:
    print("El primer numero es menor que el segundo")

