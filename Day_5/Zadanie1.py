# Usuń duplikaty z listy

lista = [10, 20, 30, 40, 20, 45, 20, 10, 49, 90, 35, 40]
list_bez_duplik = []

for element in lista:
    if element not in list_bez_duplik:
        list_bez_duplik.append(element)
    else:
        continue

print(list_bez_duplik)

lista = list_bez_duplik

print(lista)

