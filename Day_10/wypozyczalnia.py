from Day_10.klient import Klient
from Day_10.film import Film

kl1 = Klient("Adam", 89123402091)
kl2 = Klient("Joanna", 666666666)

film1 = Film("rambo", 15.90)
film2 = Film("Polowanie", 5.90)
film3 = Film("Czas", 25.90)

kl1.wypozycz(film1)

print(film1)
print(film2)
print(film3)

film3.kategoria = "Dramat"

print(film3.kategoria)
#print(film2.kategoria)

