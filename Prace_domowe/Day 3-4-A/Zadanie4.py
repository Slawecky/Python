# oblicz ocenę na podstawie progu procent
# Kryterium ocen z AWF'u
# 30% - 40% 2, 41%-60% 3, 61% - 78% 4, 79% - 94% 5, 95% -100% 6

ocena = " Słabiutko"
wynik = int(input( "Podaj swój wynik procentowy i nie wtryniaj literek bo się program wywali : "))

if wynik < 30:
    ocena = " Ucz się dalej !"
elif wynik <= 40:
    ocena = " Pała trochę lepiej niż w zeszłym roku"
elif wynik <= 60:
    ocena = " Trója brawo !"
elif wynik <= 78:
    ocena = " Czwórka ? A łyżka na to niemożliwe !"
elif wynik <= 94:
    ocena = " Piątka ? mama za Ciebie pisała ?"
elif wynik <= 100:
    ocena = " Szóstka ? Daj mi pospać jeszcze pół godziny i potem obudź"
print(f"Hmm {wynik} % to {ocena}")

# Standardowo zabezpieczenia input error kiedy indziej
