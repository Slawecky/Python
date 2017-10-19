from unittest import TestCase
from Day_13.kalk import *

class KalkTesty(TestCase):

    def setUp(self):
        self.a = 10
        self.b = 2

    def test_dodaj(self):

        suma_oczekiwana = self.a + self.b
        #act
        suma_rzeczywista = dodaj(self.a, self.b)

        self.assertEqual(suma_oczekiwana, suma_rzeczywista)

    def test_pomnoz(self):
        a = 11
        b = 13
        iloczyn_oczekiwany = a* b
        iloczyn_rzeczywisty = pomnoz(a,b)
        self.assertEqual(iloczyn_oczekiwany, iloczyn_rzeczywisty)

    def test_odejmij(self):
        wart_oczek = self.a - self.b
        wart_oczek += '\n'
        wart_rzecz = get_print_output(odejmij(self.a, self.b))
        self.assertEqual(wart_oczek, wart_rzecz)