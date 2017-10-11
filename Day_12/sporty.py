from Day_12.zawodnik import Zawodnik

z1 = Zawodnik("Dzidzia", "Ręczna")

print(z1.imie)
print(z1.dyscyplina)
# print(z1.__numer_koszulki)
z1.ustaw_nr_koszulki(123)

z1.wypisz_numer()

z1.czy_zarabia(5000)
z1._Zawodnik__zarobki = 200
print(z1._Zawodnik__zarobki)
print(z1.__dict__)


