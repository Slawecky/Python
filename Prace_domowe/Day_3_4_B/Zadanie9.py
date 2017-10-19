# if elif else
# oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata

wiek_psa = int(input("Podaj wiek psa :"))

if wiek_psa <=2 :
    print(f"Twój pies gdyby był człowiekiem miałby : {wiek_psa*10.5} lat")
elif wiek_psa <=28:
    print(f"Twój pies gdyby był człowiekiem miałby : {(wiek_psa-2) * 4 + 21} lat")
else:
    print(("Twój pies pobił rekor Guinessa !"))
