plik = open("dane.txt")

linijka = plik.readline()
linijka1 = plik.readline()
print(linijka, end='')
print(linijka1, end='')
pozostaly_tekst = plik.read()
print(pozostaly_tekst)

plik.close()
