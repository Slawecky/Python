# Kolejka pierwszy przyszłu pierwsze poszło - FiFo

kolejka = []

kolejka.append(1)
kolejka.append(56)
kolejka.append(23)

print(kolejka)

element = kolejka.pop(0)
print(element)
print(kolejka)
kolejka.append(45)
kolejka.pop(0)
print(kolejka)

# stos - LiFo

stos = []

stos = [666, 333, 999, 55555]
stos.append(87)
stos.append(123)
stos.append(765)
print(stos)

element2 = stos.pop()
print(element2)
print(stos)


