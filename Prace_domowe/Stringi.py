# Do wykonania :
# Napisać program, który zmieni string wejściowy „Ala ma kota, kot ma 4nogi.” na string „Arek lubi psy, a najbardziej boksery!”
# Nie wolno dostarczać bezpośrednio literek!!! Można dowolnie przekształcać string wejściowy.


string_we = "Ala ma kota, kot ma 4 nogi."
string_wy = "Arek lubi psy, a najbardziej boksery!"



# Test zmiennych

print(" Stringi z zadania :\n")
print(string_we)
print(f"{string_wy}\n")


# Ilość znaków w zmiennych i różnice

dlugosc_we = len(string_we)
dlugosc_wy = len(string_wy)
roznica = abs(dlugosc_we-dlugosc_wy)

print("Ilości znaków i różnica")
print(f"String wejściowy: \"{string_we}\" ma  {dlugosc_we} znaków")
print(f"String wyjściowy: \"{string_wy}\" ma  {dlugosc_wy} znaków\n")
print(f" Róznica w ilości znaków to {roznica}\n")

# Znaki ASCII

print("String wejściowy w ASCII\n")
print(ord(string_we[0]), ord(string_we[1]), ord(string_we[2]), ord(string_we[3]), ord(string_we[4]), ord(string_we[5]), ord(string_we[6]))
print(ord(string_we[byte]))


