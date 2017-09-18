# obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

print("Podaj zakres lat do obliczenia który rok jest przestępny")
pocz = int(input("Podaj początkowy rok :    "))
kon = int(input("Podaj koncowy rok :    "))


lata = range(pocz, kon)

for rok in lata:
    if rok % 4 == 0 or rok % 400 == 0 and rok % 100 != 0:
        print(rok, " Rok przestępny ")
    elif rok % 4 > 0 or rok % 400 > 0 and rok %100 == 0:
            print(rok, " Rok nieprzestępny ")

# Do dorobienia warunki podawania zakresu
