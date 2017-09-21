# Sprawdzić czy string jest palindromem

from Day_6.Fun7 import odwoc_str

def czy_palindrom(fraza:str):

    for litera1, litera2 in zip(fraza, odwoc_str(fraza)):
        if litera1 != litera2:
            return False
        return True

czy_palindrom("kajak")
czy_palindrom("bajka")
