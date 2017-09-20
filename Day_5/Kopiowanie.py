# kopiowanie list z typami prostymi

wynik = 3

lista_a = ["zero", "jeden", wynik]
print("list a: ", lista_a)

wynik = 43

print("list a: ", lista_a)

lista_b = lista_a.copy()
print("list b ", lista_b)

lista_a.append("nowy")
print("list a: ", lista_a)
print("list a: ", lista_b)

print(hex(id(lista_a)))
print(hex(id(lista_b)))
