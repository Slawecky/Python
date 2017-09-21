def dodaj_imie(imie, imiona=None):
    if imiona == None:
        imiona = []
    imiona.append(imie)
    return imiona

#baza = []

baza = dodaj_imie("Marta")
print(baza)
dodaj_imie("Marek", baza)
print(baza)

anglicy = dodaj_imie("Tommy")
print(anglicy)

francuzi = dodaj_imie("Pierre")
print(francuzi)

def policz(a,b):
    return (a**2, b**3)
x, y = policz(3,4)

print(x)
print(y)
