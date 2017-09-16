# Min 6 znaków, liczby i litery

haslo = input(" Podaj hasło nie krótsze niż 6 znaków : ")

prawidlowe = False

while not prawidlowe:
    if len(haslo) < 6:
        prawidlowe = False
        print(" Za krótkie hasło !!!")
    else:
        prawidlowe = True

    if haslo.isalpha():
        print("Hasło musi zawierać cyfry")
        prawidlowe = False
    else:
        prawidlowe = True

    if haslo.isnumeric():
        print("Hasło musi zawierać litery")
        prawidlowe = False
    else:
        prawidlowe = True

    if not prawidlowe:
        haslo = input("Podaj hasło jeszcze raz : ")

print("Hasło prawidłowe")