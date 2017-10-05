from Day_10.czlowiek import Czlowiek

class Student(Czlowiek):
    def __init__(self,imie, wiek, indeks):
        self.indeks = indeks
    def biega(self):
        print(f"Student {self.imie} bieg do tyłu")
    def halasuj(self):
        print(f"Pan da trzy")
