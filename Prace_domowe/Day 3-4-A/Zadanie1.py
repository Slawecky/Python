#   sprawdź czy jest wygrana w kółko i krzyżyk
#   input: string 9 znaków x, o, n
#   znaki oznaczają pozycje wierszami od górnego


gra = input("Podaj wynik gry w k&k X, 0, N ( 9 znaków bez spacji przecinków itp. : ")
if len(gra) == 9:
# poziomo
    if gra.index("XXX") == 0:
        print("Wygrana X")
        if gra.index(""):
            print(" Coś nie haloo")


print(" Dorobię kiedy indziej")

# Do sprawdzenia czy koncepcja jest OK
