try:
    with open("lala") as plik:
        print(plik.read())

except FileNotFoundError as error:
    print("Nie ma takiego pliku")
    print(error)

except NameError:
    print("Nie ma zmiennej")

except Exception:
    print("Pojawił się jakiś błąd")
