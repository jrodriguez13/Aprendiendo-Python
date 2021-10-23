# # ***** CALCULADORA INICIAL *****
fin = False
print("""***********
Calculadora
***********
Menu
1)Suma
2)Resta
3)Multiplicacion
4)Division
5)Salir""""")
while not fin:
    opc = int(input("Opcion:"))
    if opc == 1:
        sum1 = int(input("Sumando uno:"))
        sum2 = int(input("Sumando dos:"))
        print("La suma es:", sum1 + sum2)
    elif opc == 2:
        minuendo = int(input("minuendo:"))
        sustraendo = int(input("sustraendo:"))
        print("la resta es:", minuendo - sustraendo)
    elif opc == 3:
        multiplicando = int(input("multiplicando:"))
        multiplicador = int(input("multiplicador:"))
        print("la multiplicacion es:", multiplicando*multiplicador)
    elif opc == 4:
        dividendo = int(input("dividendo:"))
        divisor = int(input("divisor:"))
        print("la division es:", dividendo / divisor)
    elif opc == 5:
        fin = True
    else:
        print("Opción incorrecta. Reingrese \n")