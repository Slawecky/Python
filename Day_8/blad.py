import os

sciezka = "lalal"
if os.path.exists(sciezka):
    with open("lalal") as plik:
        zawartosc = plik.read()
        print(zawartosc)
else:
    print("Plik nie istnieje")
