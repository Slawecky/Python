with open("dane.txt") as plik:
    print(plik.tell())
    linijka = plik.readline()
    print(plik.tell())
    znak = plik.read(1)
    print(znak)
    print(plik.tell())

    plik.seek(2)
    print(plik.read(1))
    print(plik.tell())
