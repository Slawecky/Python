baza = []

with open("osoby.csv", "r+") as plik:

    # lista kolumn - opis
    opis = plik.readline()
    print(opis.strip())
    print(opis)

    for linijka in plik:
        # Usuwamy whitespace
        linijka = linijka.strip()

        osoba = linijka.split(",")
        print(osoba)
        baza.append(osoba)

    baza.append(["Jan", "kowalski", "47"])

    dane_zapis = []
    for osoba in baza:
        osoba = ",".join(osoba)
        dane_zapis.append(osoba + "\n")

    plik.seek(0)
    plik.writelines(dane_zapis)
print(baza)

