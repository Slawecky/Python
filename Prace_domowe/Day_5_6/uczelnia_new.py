# Program - baza nowych studentów
# Opcje do wyboru
# 1. Dodaj studenta
# 2. Usuń studenta
# 3. Wyszukaj studenta
# 4. Pokaż listę studentów
# ...
# x. zakończ program

from Prace_domowe.Day_5_6.opcje import *
# lista = []

def menu_kl():

    menu = {'1': "Dodaj studenta", '2': "Usuń studenta", '3': "Wyszukaj studenta", '4': "Pokaż listę studentów ",
            '..': "", '9': "Zakończ program\n"}
    while True:
        wybor = menu.keys()
        print("\n Witam w systemie Comsite Uczelnia 2017,\n")
        for inp in wybor:
            print(inp, menu[inp])
        przycisk = input("Wybierz odpowiedni klawisz: ")
        print("\n")
        if przycisk == '1':
            dodaj()
        elif przycisk == "2":
            usun()
        elif przycisk == '3':
            wyszukaj()
        elif przycisk == '4':
            wypisz()
        elif przycisk == '9':
            print("Dziękujemy za pracę z naszym programem")
            break
        else:
            print("Nie ten klawisz, wybierz ponownie")

menu_kl()








