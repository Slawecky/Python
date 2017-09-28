try:
    with open("dane.txt") as plik:
        print(plik.read())
except FileNotFoundError as e:
    print(e)
    print("Podany plik nie istnieje !")
    #raise ValueError("Błedna warość scieżki")
except Exception:
    print(" Nieoczekiwany błąd")
print(" Dalsza część programu")