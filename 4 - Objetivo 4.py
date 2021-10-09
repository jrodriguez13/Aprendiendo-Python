# ***** BUCLES *******
# i = 0
# while i<10:
#     print(i,end=" ")
#     i = i + 1

# continuar = True
# while continuar:
#     valor = int(input("ingrese un numero superior a 100:"))
#     if valor>100:
#         continuar=False
# print("programa acabado")

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for item in lista:
#     print(item, end=" ")

# lista = ["computadora", "teclado", "mouse"]
# for item in lista:
#     print(item, end=" ")

# for item in range(10):
#    print(item, end=" ")

# for item1 in range(3):
#     for item2 in range(5):
#         print("item1 =" + str(item1) + ", item2 =" + str(item2))

# item1 = 0
# while item1 < 3:
#     for item2 in range(5):
#         print("item1 =" + str(item1) + ",item2 =" + str(item2))
#     item1 = item1 + 1

item1 = 0
while item1 <3:
    item2 = 0
    while item2<5:
        print("item1 = " + str(item1) + ",item2 = " + str(item2))
        item2 = item2 + 1
    item1 = item1 + 1
