def wypisz_dane(imie, nazwisko, kurs="Python", il_dni=15):
    print(imie, nazwisko, kurs, il_dni)
wypisz_dane("Sławek", "Cygert")
wypisz_dane("Sławek", "Cygert", "Java")
wypisz_dane("Jan", "Matejko", "malarstwo", 365)
wypisz_dane("Paulina", "K", 30)

wypisz_dane("Marek", "O", il_dni=66)

wypisz_dane(kurs="Java", imie="Olaf", il_dni=33, nazwisko="Jafa")
