lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista1 = []

for e in lista:
    lista1.append(e**2)
print(lista)
print(lista1)

lista3 =[x**2 for x in lista]

print(lista3)

lista4 = [x**3 for x in lista if x % 3 == 0]

zakre_lista = [x**2 for x in range(10)]
print(zakre_lista)
