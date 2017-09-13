# Sprawdź czy liczba jest podzielna przez 3 i 5 i 7

liczba = input("podaj liczbe")

# Sprawdź czy liczba jest prawidłowa
if liczba.isnumeric():
    liczba = int(liczba)
    if liczba % 3 ==0:
        print(f"{liczba} Jest podzielna przez 3 ")
    if liczba % 5 ==0:
        print(f"{liczba} Jest podzielna przez 5 ")
    if liczba % 7==0:
        print(f"{liczba} Jest podzielna przez 5 ")