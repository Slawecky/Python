# Listy
lista = ["keden", "trzy"]
lista1 = [1, "dwa", "trzy", 5]
lista2 = list(range(2,6))
lista3 = list("Kwiatek")
print(lista)
print(lista1)
print(lista2)
print(lista3)

flower = ""

for znak in lista3:
    flower += znak.upper()

print(flower)

flower2 = " ".join(lista3)
print(flower2)

