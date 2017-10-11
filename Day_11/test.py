class A(object):
    podwyzka = 0.005
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
osoba1 = A("Slaw", "Cygert")
print(osoba1.podwyzka)
print(osoba1.pesel)
