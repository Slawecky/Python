with open ( "dane.txt", "w" ) as plik:
    print(plik.tell())

    s1 = "ala ma kota"
    s2 = "Antoni Gąbka"
    s3 = "Policjanci z jajami\n"

    lista = [s1, s2, s3]
    plik.writelines(lista)

    plik.writelines([s+'\n' for s in lista])
