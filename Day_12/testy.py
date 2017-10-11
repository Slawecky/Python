from unittest import TestCase
from Day_12.zawodnik import Zawodnik

class TestZawodnik(TestCase):

    def setUp(self):
        self.zawodnik = Zawodnik("Jan", "pilka")

    def test_init(self):

        self.assertEquals("Jan", self.zawodnik.imie)

    def test_ustaw_nr_koszulki(self):

        self.zawodnik.ustaw_nr_koszulki(23)


        self.assertEquals(23, self.zawodnik.ustaw_nr_koszulki())
