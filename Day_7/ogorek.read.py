import pickle

baza_odtworzona = None
with open("baza.bak", "rb") as plik:
    baza_odtworzona = pickle.load(plik)
print(type(baza_odtworzona))
print(baza_odtworzona)

print(locals())
print(globals())