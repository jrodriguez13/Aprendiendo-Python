# ------- OBJETIVO 2 -------

# OPERADOR DE ASIGNACIÓN

# precio = 1200
# apellido = "Gurruchaga"
# numero = 67

# OPERADORES ARITMÉTICOS

# resultadomultiplicacion = 8 * 4
# coste = (6*11)-4
# salasdecine = 50/4

# OPERADORES RELACIONALES

# print(7<5)
# print(9==3)
# print(2<12)
# print(88>=4)

# OPERADORES LÓGICOS

# print((2<3) and (4==4))
# print((8<7) or (4==3))
# print(not(6==7))
# print(True and False)

# EJERCICIO 1

# sumando1 = int(input("ingrese el primer numero:"))
# sumando2 = int(input("ingrese el segundo numero:"))
# print("resultado de la suma:", sumando1 + sumando2)

# EJERCICIO 2

# sumando1 = float(input("ingrese primer numero(decimal):"))
# sumando2 = float(input("ingrese segundo numero(decimal):"))
# print("resultado de la suma", sumando1 + sumando2)

# EJERCICIO 3

# minuendo = int(input("Introduzca el minuendo: "))
# sustraendo = int(input("Introduzca el sustraendo: "))
# print("Resultado de la resta: ", minuendo - sustraendo)

# EJERCICIO 4

# minuendo = float(input("Introduzca el minuendo: "))
# sustraendo = float(input("Introduzca el sustraendo: "))
# print("Resultado de la resta: ", minuendo - sustraendo)

# EJERCICIO 5

# multiplicando = int(input("Introduzca el multiplicando: "))
# multiplicador = int(input("Introduzca el multiplicador: "))
# print("Resultado de la multiplicacion: ", multiplicando * multiplicador)

# EJERCICIO 6

# multiplicando = float(input("Introduzca el multiplicando: "))
# multiplicador = float(input("Introduzca el multiplicador: "))
# print("Resultado de la multiplicacion: ", multiplicando * multiplicador)

# EJERCICIO 7

# dividendo = int(input("Introduzca el dividendo: "))
# divisor = int(input("Introduzca el divisor: "))
# print("Resultado de la división: ", dividendo / divisor)

# EJERCICIO 8

# dividendo = float(input("Introduzca el dividendo: "))
# divisor = float(input("Introduzca el divisor: "))
# print("Resultado de la division: ", dividendo / divisor)

# EJERCICIO 9

# dividendo = float(input("ingrese el dividendo:"))
# divisor = float(input("ingrese divisor:"))
# resultado = round(dividendo/divisor, 3)
# print("resultado de la division", resultado)

# CADENAS DE TEXTO (BASICO)

# frase = "hola! me llamo Javier, como estas?"
# print(frase)

# frase = "hola!\"me llamo Javier,\"como estas?"
# print(frase)

# ***** FASE 3 COLECCIONES *******

# # ***** LISTAS *****
# lista = ["computadora", "teclado", "mouse"]
# print(lista)

# lista = ["computadora", "teclado", "mouse"]
# print(len(lista))
# print(lista[0])
# print(lista[1])
# print(lista[2])

# listaoriginal = ["computadora", "teclado", "mouse"]
# listanueva = ["monitor","impresora","parlantes"]
# listafinal = listanueva + listaoriginal
# print(listafinal)

# lista = ["computadora", "teclado", "mouse"]
# print(len(lista))
# lista = lista + ["mesa"]
# print(len(lista))

# lista = ["computadora", "teclado", "mouse"]
# print(lista)
# lista[0] = "monitor"
# lista[1] = "impresora"
# lista[2] = "parlantes"
# print(lista)

# lista = ["computadora", "teclado", "mouse"]
# print(lista)
# del lista[1]
# print(lista)


# lista = ["computadora", "teclado", "mouse", ["placa de sonido", "microfono", "parlantes"]]
# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])
# print(lista[3][0])
# print(lista[3][1])
# print(lista[3][2])

# #***** TUPLAS *****
# tupla = ("computadora", "teclado", "mouse")
# print(tupla)
# print(len(tupla))
# print(tupla[0])
# print(tupla[1])
# print(tupla[2])


# ***** DICCIONARIOS *****
# mesestraducidos = {"Enero": "January",
#                    "Febrero": "February",
#                    "Marzo": "March",
#                    "Abril": "April",
#                    "Mayo": "May",
#                    "Junio": "June",
#                    "Julio": "July",
#                    "Agosto": "August",
#                    "Septiembre": "September",
#                    "Octubre": "October",
#                    "Noviembre": "November",
#                    "Diciembre": "December"}
# print(mesestraducidos["Noviembre"])
# print(mesestraducidos["Mayo"])

# # ***** BOOLEANOS Y OPERADORES LOGICOS *****
# variablebooleana = True
# print(variablebooleana)

# variablebooleana = False
# print(variablebooleana)

# booleano1 = True
# booleano2 = True
# print(booleano1 and booleano2)

# booleano1 = True
# booleano2 = False
# print(booleano1 and booleano2)

# booleano1 = False
# booleano2 = False
# print(booleano1 and booleano2)

# booleano1 = True
# booleano2 = True
# print(booleano1 or booleano2)

# booleano1 = True
# booleano2 = False
# print(booleano1 or booleano2)

# booleano1 = False
# booleano2 = False
# print(booleano1 or booleano2)

# booleano = False
# print(not booleano)

# ****** OPERADORES RELACIONALES ******

# numero1 = 6
# numero2 = 9
# print(numero1 > numero2)
# print(numero1 >= numero2)
# print(numero1 < numero2)
# print(numero1 <= numero2)
# print(numero1 == numero2)
# print(numero1 != numero2)

# ****** CADENAS DE TEXTO (AVANZADO) *******

# cadenaejemplo = "en un lugar de buenos aires..."
# print(cadenaejemplo.capitalize())

# cadenaejemplo = "en un lugar de buenos aires..."
# print(cadenaejemplo.upper())

# cadenaejemplo = "EN UN LUGAR DE buenos aires..."
# print(cadenaejemplo.lower())

# cadenaejemplo = "En un lugar de buenos aires..."
# print(len(cadenaejemplo))

# cadenaejemplo = "En un lugar de buenos aires..."
# print(cadenaejemplo.isalnum())
# cadenaejemplo = "1234567890"
# print(cadenaejemplo.isalnum())
# cadenaejemplo = "abcdefg1234567890"
# print(cadenaejemplo.isalnum())
# cadenaejemplo = "abcdefg 1234567890"
# print(cadenaejemplo.isalnum())

# cadenaejemplo = "Enunlugardebuenosaires"
# print(cadenaejemplo.isalpha())
# cadenaejemplo = "En un lugar de buenos aires"
# print(cadenaejemplo.isalpha())
# cadenaejemplo = "1234567890"
# print(cadenaejemplo.isalpha())
# cadenaejemplo = "abcdefg 1234567890"
# print(cadenaejemplo.isalpha())

# cadenaejemplo = "En un lugar de buenos aires"
# print(cadenaejemplo.isdigit())
# cadenaejemplo = "1234567890"
# print(cadenaejemplo.isdigit())
# cadenaejemplo = "abcdefg 1234567890"
# print(cadenaejemplo.isdigit())

# cadenaejemplo = "En un lugar de Buenos Aires"
# print(cadenaejemplo.islower())
# cadenaejemplo = "en un lugar de buenos aires"
# print(cadenaejemplo.islower())

# cadenaejemplo = "En un lugar de Buenos Aires"
# print(cadenaejemplo.isupper())
# cadenaejemplo = "EN UN LUGAR DE BUENOS AIRES"
# print(cadenaejemplo.isupper())

# cadenaejemplo = " En un lugar de buenos aires"
# print(cadenaejemplo.lstrip())
# cadenaejemplo = " En un lugar de buenos aires      "
# print(cadenaejemplo.rstrip())
# cadenaejemplo = " En un lugar de buenos aires "
# print(cadenaejemplo.strip())

# cadenaejemplo = "abcdefghijklmnopqrstuvwxyz0123456789"
# print(max(cadenaejemplo))
# print(min(cadenaejemplo))

# cadenaejemplo = "AAAAEIIIOUUU"
# print(cadenaejemplo.replace('A','E'))
# print(cadenaejemplo.replace('I','D'))
# cadena2 = cadenaejemplo.replace('U', '8')
# print(cadena2)

# cadenaejemplo = "En un lugar de buenos aires"
# print(cadenaejemplo.swapcase())

# cadenaejemplo = "En un lugar de buenos aires"
# print(cadenaejemplo.split())

# cadenaejemplo = "31/12/2020"
# print(cadenaejemplo.split('0'))