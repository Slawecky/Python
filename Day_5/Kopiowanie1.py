import copy

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "ludwik"]

zakupy_wrzesiń =[nabial, chemia]
print("Wrzesień : ", zakupy_wrzesiń)

zakupy_pazdzienik = zakupy_wrzesiń.copy()
print("Pażdziernik ; ", zakupy_pazdzienik)

zakupy_listopad = [x for x in zakupy_wrzesiń]
print("listopad : ", zakupy_listopad)

zakupy_grudzień = copy.deepcopy(zakupy_wrzesiń)

zakupy_wrzesiń[1].append("gąbki")
print("Wrzesień : ", zakupy_wrzesiń)
print("Pażdziernik : ", zakupy_pazdzienik)
print("listopad : ", zakupy_listopad)
print("listopad : ", zakupy_grudzień)

print(id(zakupy_wrzesiń))
print(id(zakupy_listopad))
print(id(zakupy_listopad))
print(id(zakupy_grudzień))

