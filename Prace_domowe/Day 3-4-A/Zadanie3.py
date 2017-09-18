# Sprawdź czy liczba jest podzielna przez 3 i 5 i 7

liczba = input("podaj liczbe")

# Sprawdź czy liczba jest prawidłowa
if liczba.isnumeric():
    liczba = int(liczba)
    print("to jest liczba : ", liczba)
    if liczba % 3 == 0:
        if liczba % 5 == 0:
            if liczba % 7 == 0:
                print (" :Liczba jest podzielna przez 3 i 5 i 7")

            else:
                print("Podaj liczbę !")