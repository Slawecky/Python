# program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie

pocz = int(input("Podaj początek zakresu : "))
kon = int(input("Podaj koniec zakresu : "))
parz = 0
niep = 0
zakres = range(pocz, kon)

for liczba in zakres:
    if liczba % 2 == 0:
        parz += 1
    else:
        niep += 1

print(f"Ilość liczb parzystych w zakresie : {parz}")
print(f"Ilość liczb nieparzystych w zakresie : {niep}")

