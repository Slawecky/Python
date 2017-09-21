def drukuj_kwadraty():
    liczby = range(12)
    for l in liczby:
        print(l**2)
drukuj_kwadraty()

x= drukuj_kwadraty
# x= drukuj_kwadraty()

print(x)
print(type(x))
x()

