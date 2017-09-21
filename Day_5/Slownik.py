#osoby = dict()
osoby = {"Ania":"Kowalska", 2:234.4, "9238732": 4}
liczby = {0:1, 1:2, 2:3, 3:4}
osoby["Joanna"] = "Policja"

print(osoby[2])
print(liczby[1])
print(osoby)
osoby["Joanna"] = "Straż"
print(osoby)



print(osoby.keys())
print(osoby.values())


for key, value in osoby.items():
    print(f"Klucz : {key} - Wartość: {value}")
