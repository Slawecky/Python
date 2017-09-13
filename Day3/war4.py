imie = input("Podaj imię : ")

if"a" in imie:
    print("Litera a jest w imieniu")
elif"A" in imie:
    print("Litera A jest w imieniu")
else:
    imie = imie.upper()
    print("W imieniu nie ma liter A i a")
    print(2 * imie)
print("Koniec")
