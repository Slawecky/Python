kolekcja_a = "123456789666"
kolekcja_b = "Ala ma kota albo dwa"

# for (el_a, el_b) in zip(kolekcja_b, kolekcja_a):
#    print(el_a, el_b)

indeks = 0
for el_a in kolekcja_a:
    print(el_a), kolekcja_b[indeks]
    indeks += 1
