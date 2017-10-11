from Day_11.metody_klasy1 import Pracownik

prac1 = Pracownik("John Turturo", "aktor")
prac2 = Pracownik("John Travolta", "gwiazda")

print(prac1)
print(prac2)

prac2.ustaw_pensje(10500)
print(prac2)

prac2.daj_podwyzke(5)
print(prac2)

prac1.roczna_podw = 7
print("\n Ilość pracowników (klasa, obiekt1, obiekt2")
print(Pracownik.ilosc_pracownikow)
print(prac1.ilosc_pracownikow)
print(prac2.ilosc_pracownikow)

print("\n Roczna podwyżka (klasa, obiekt1, obiekt2")
print(Pracownik.roczna_podw)
print(prac1.roczna_podw)
print(prac2.roczna_podw)

print("Pracownik : ")
print(Pracownik.__dict__)
print()

del prac1.roczna_podw

print("Pracownik1 : ")
print(prac1.__dict__)
print()

print("Pracownik2 : ")
print(prac2.__dict__)
print()

