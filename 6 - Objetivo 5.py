# # ***** FUNCIONES *****

# def Saludar():
#    print("hola mundo")

# # Main
# Saludar()


# def EsMayorQueCero(param):
#     if param > 0:
#         print(param, "es mayor que cero")
#     elif param == 0:
#         print(param, "es igual a cero")
#     else:
#         print(param, "es menor que cero")

# #Main
# numero = int(input("introduce un numero:"))
# EsMayorQueCero(numero)


# def Sumar(param1, param2):
#     return param1 + param2

# #Main
# sumando1 = int(input("Introduce el primer sumando: "))
# sumando2 = int(input("Introduce el segundo sumando: "))
# resultado = Sumar(sumando1,sumando2)
# print("El resultado de la suma es: ", resultado)



# def SumarRestar(param1, param2):
#     return param1 + param2, param1 - param2

# #Main
# numero1 = int(input("Introduce el primer numero: "))
# numero2 = int(input("Introduce el segundo numero: "))
# resultadosuma, resultadoresta = SumarRestar(numero1,numero2)
# print("El resultado de la suma es: ", resultadosuma)
# print("El resultado de la resta es: ", resultadoresta)



# def Sumar(*valores):
#     resultado = 0
#     for item in valores:
#         resultado = resultado + item
#     return resultado

# #Main
# resultado = Sumar(23,56,3,89,78,455)
# resultado2 = Sumar(1,2,4,5,767,67645,8)
# print("El resultado de la suma es: ", resultado)
# print("El resultado de la suma es: ", resultado2)



def SumarRestar(param1, param2):
    return Sumar(param1,param2), Restar(param1,param2)

def Sumar(sumando1, sumando2):
    return sumando1 + sumando2

def Restar(minuendo, sustraendo):
    return minuendo - sustraendo

#Main
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
resultadosuma, resultadoresta = SumarRestar(numero1,numero2)
print("El resultado de la suma es: ", resultadosuma)
print("El resultado de la resta es: ", resultadoresta)