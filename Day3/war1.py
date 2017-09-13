# if

if True:
    pass

x = 5
#y = int(input("podaj liczbę całkowitą :    "))
y = (input("podaj liczbę całkowitą :    "))
print(y)
print(type(y))
# Wszystkien inputy są stringiem

if y.isnumeric():
    print("To jest liczba")
if x < int(y):
    print(f"{x} jest mniejszy od Twojej liczby")
    if int(y) > 10:
        print("Twoja liczba jest większa od 10")

print("koniec programu")