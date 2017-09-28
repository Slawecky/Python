import pickle

baza = [
    ["Adam", "Darski", "Nergal", 34],
    ["Jarek", "Nowak", "NN", 47]
]

with open("baza.bak", "wb") as plik:
    pickle.dump(baza, plik)
    print("zapisano")
