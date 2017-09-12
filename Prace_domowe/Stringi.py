# Do wykonania :
# Napisać program, który zmieni string wejściowy „Ala ma kota, kot ma 4nogi.” na string „Arek lubi psy, a najbardziej boksery!”
# Nie wolno dostarczać bezpośrednio literek!!! Można dowolnie przekształcać string wejściowy.


string_we = "Ala ma kota, kot ma 4 nogi."
string_wy = "Arek lubi psy, a najbardziej boksery!"



# Test zmiennych

print(" Stringi z zadania :\n")
print("String wejściowy : ", string_we)
print("String wyjściowy : ", string_wy)
print("\n")



# Ilość znaków w zmiennych i różnice

dlugosc_we = len(string_we)
dlugosc_wy = len(string_wy)
roznica = abs(dlugosc_we-dlugosc_wy)

print("Ilości znaków i różnica.\n")
print(f"String wejściowy: \"{string_we}\" ma  {dlugosc_we} znaków")
print(f"String wyjściowy: \"{string_wy}\" ma  {dlugosc_wy} znaków\n")
print(f" Róznica w ilości znaków to {roznica}\n")

# Wersja pierwsza

print("Zmieniamy po wyrazie : .\n")

string_we1 = (string_we.replace("Ala","Arek"))
print(string_we1)
string_we2 = (string_we1.replace("ma", "lubi",1))
print(string_we2)
string_we3 = (string_we2.replace("kota","psy"))
print(string_we3)
string_we4 = (string_we3.replace("kot","a"))
print(string_we4)
string_we5 = (string_we4.replace("ma 4","najbardziej"))
print(string_we5)
string_we6 = (string_we5.replace("nogi.","boksery!"))
print(string_we6)
print("\n")

# Porównanie

print("Porównanie : \n")
print("String wejściowy             : ", string_we)
print("String wyjściowy             : ", string_wy)
print("String wejściowy zmieniony   : ", string_we6)
print("\n")
print(f"Niby to samo ale coś nie halo   : {string_we6 is string_wy}")
print(f"A tak OK ???                    : {string_we6 == string_wy}\n")

# Porównanie drugie ( Typu włoskiego )

Test1 = list(string_we6)
Test2 = list(string_wy)
print(f"List wejściowy zmieniony     :{Test1}")
print(f"List wyjściowy               :{Test2}")

print("ASCII wejściowy zmieniony    : ", ', '.join(str(ord(c)) for c in string_we6))
print("ASCII wyjściowy              : ", ', '.join(str(ord(c)) for c in string_wy))

print(f"Po zmianie na list znowu to samo    : {Test1 is Test2}")
print(f"Trzeba poczytać  == a is            : {Test1 == Test2}")

