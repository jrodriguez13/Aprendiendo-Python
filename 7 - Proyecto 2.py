# ***** CALCULADORA *****

def Sumar():
    sum1 = int(input("Sumando uno:"))
    sum2 = int(input("Sumando dos:"))
    print("La suma es:", sum1 + sum2)

def Restar():
    minuendo = int(input("minuendo:"))
    sustraendo = int(input("sustraendo:"))
    print("la resta es:", minuendo - sustraendo)

def Multiplicar():
    multiplicando = int(input("multiplicando:"))
    multiplicador = int(input("multiplicador:"))
    print("la multiplicacion es:", multiplicando*multiplicador)

def Dividir():
    dividendo = int(input("Dividendo:"))
    divisor = int(input("Divisor:"))
    print("la division es:", dividendo / divisor) 


def Modulo():
    variable = int(input("Ingrese un numero: "))
    print("El modulo resto es: ", variable%2)


def Calculadora():
    fin = False
    while not(fin):
        opc = int(input("Opcion:"))
        if(opc == 1):
            Sumar()
        elif(opc == 2):
            Restar()
        elif(opc == 3):
            Multiplicar()
        elif(opc == 4):
            Dividir()
        elif(opc == 5):
            Modulo()
        elif(opc == 6):
            fin = 1
        else:
            print("Opción incorrecta. Reingrese \n")     


# ***** MAIN *****

print("""***********
Calculadora
***********
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Modulo resto
6) Salir""""")
Calculadora()
