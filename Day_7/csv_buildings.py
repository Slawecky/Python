import csv

with open("osoby.csv") as plik:
    # Tworzymy czytnik

    czytnik_csv = csv.reader(plik)
    for line in czytnik_csv:
        print(line)

dane = ["adam", "Kowalski", 33]

with open("osoby.csv", "a") as plik:
    # tworzę zapisywacz
    zapisywacz_csv = csv.writer(plik)
    zapisywacz_csv.writerow(dane)

