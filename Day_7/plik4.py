with open("dane.txt", "r+") as plik:

    plik.seek(1)
    znak = plik.read(1)

    if znak == "\n":
        plik.write("Moja dopisana linijka")
    else:
        plik.write("\n Moje")

