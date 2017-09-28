plik = open("dane.txt", "r", encoding='utf8')

print(plik.readline(), end="")

linijki = plik.readlines()
print(linijki)

plik.close()