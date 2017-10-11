from Day_11.zwierz import zwierz

class kon (zwierz):
    def __init__(self, imie):
        zwierz.__init__(self, imie)
    def say(self):
        print(f"{self.name} rży ")
    def skok(self):
        print(f"Koń {self.name} skacze!")
