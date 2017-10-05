from Day_10.zwierze import Zwierze
from Day_10.czlowiek import Czlowiek
from Day_10.pies import Pies
from Day_10.student import Student

# Tworzymy zwierzaka

zwierz = Zwierze("Kaszmir")
zwierz.biega()
zwierz.halasuj()

# Człowiek

czlek = Czlowiek("Stefan", 34)
czlek.biega()
czlek.halasuj()

psina = Pies("Azor")

psina.halasuj()

czlek.podaj_wiek()

studenciak = Student("Miki", 19, 6)

studenciak.halasuj()