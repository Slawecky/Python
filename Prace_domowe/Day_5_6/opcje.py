# Opcje do programu uczelnia



lista = []


def dodaj():
    """Dodaje studenta"""
    print ( "Wprowadź dane nowego studenta" )
    imie = input ( "Podaj imię : " )
    nazwisko = input ( "Podaj nazwisko : " )
    pesel = input ( "Podaj pesel : " )
    ocena = input ( "Podaj ocenę : " )
    student = (imie, nazwisko, pesel, ocena)
    lista.append ( student )
    print ( f"Dodany student : {student}" )


def usun():
    '''Usuwa studenta'''
    print ( "Wprowadź dane studenta do usunięcia" )
    imie = input ( "Podaj imię : " )
    nazwisko = input ( "Podaj nazwisko : " )
    pesel = input ( "Podaj pesel : " )
    ocena = input ( "Podaj ocenę : " )
    student = (imie, nazwisko, pesel, ocena)
    lista.remove ( student )
    print ( f"Usunięty student : {student}" )


def wyszukaj():
    '''Wyszukuje studenta'''
    print ( "Wprowadź Pesel studenta do sprawdzenia" )
    pesel = input ( "Podaj pesel : " )
    if pesel in lista:
        print ( "Student jest w bazie" )
    else:
        print ( "Nie ma takiego studenta" )


def wypisz():
    '''Wypisuje listę studentów'''
    print ( lista )
