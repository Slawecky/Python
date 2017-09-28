with open("dane.txt", "r+") as plik:

    print(plik.tell())
    plik.read()
    poz =plik.tell()
    # przedostatnia pozycja
    plik.seek(poz -1)
    znak = plik.read(1)

    if znak == "\n":
        plik.write("Była znak nowej\n")
    else:
        plik.write("\nnie było znak nowej\n" )