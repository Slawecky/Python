class Druzyna(object):
    def __init__(self, nazwa, trener):
        self.nazwa = nazwa
        self.trener = trener
        self.__budzet = None
        self.__transfery = []

    # getter
    @property
    def budzet(self):
        if self.__budzet is None:
            return "Brak budżetu"
        else:
            return self.__budzet
    @budzet.setter
    def budzet(self, wartosc):
        try:
            self.budzet = int(wartosc)
        except:
            print("Podaj wartość liczbową")

    @property
    def transfery(self):
        if len(self.__transfery) == 0:
            return "Brak transferów"
        else:
            return self.__transfery
        
    @transfery.setter
    def transfery(self, transfer):
        if isinstance(transfer, list):
            self.__transfery.append(transfer)
        else:
            print("Podaj transfery jako listę")
