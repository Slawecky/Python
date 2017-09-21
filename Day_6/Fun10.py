def dodaj_imie(imie, imiona=[]):
    imiona.append(imie.capitalize())
    return imiona

#baza = []

nowa_baz = dodaj_imie("Marta")
print(nowa_baz)
dodaj_imie("Marek")
print(nowa_baz)

anglicy = dodaj_imie("Tommy")
print(anglicy)

francuzi = dodaj_imie("Pierre")
print(francuzi)
