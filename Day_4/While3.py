# Min 6 znaków, liczby i litery

haslo = input ( " Podaj hasło nie krótsze niż 6 znaków : " )

while len(haslo) < 6:
    print(" Za krótkie hasło !!!")
    haslo = input("Podaj hasło jeszcze raz : ")
print("Hasło prawidłowe")

