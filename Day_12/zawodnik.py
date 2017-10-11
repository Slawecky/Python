class Zawodnik(object):
    def __init__(self, imie, dyscyplina):
        self.imie = imie
        self.dyscyplina = dyscyplina
        self.__numer_koszulki = None
        self.__zarobki = None

    def ustaw_nr_koszulki(self, numer):
        if numer > 0 and numer < 100:
            self.__numer_koszulki = numer
        else:
            print(" Podaj prawidłowy numer koszulki ! ")
    @staticmethod
    def __sprawdz_numer(numer):
        if numer is None:
            return False
        else:
            return True
    def wypisz_numer(self):
        if Zawodnik.__sprawdz_numer(self.__numer_koszulki):
            print(self.__numer_koszulki)
        else:
            print(f"Zawodnik {self.imie} nie ma numeru ! ")

    def czy_zarabia(self, pensja):
        if pensja >= 1000:
            self.__zarobki = pensja
            print(f" Zarobki : {pensja} Euro")
        else:
            print("Nie wygłupiaj się")
