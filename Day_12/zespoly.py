from Day_12.druzyna import Druzyna

team1 = Druzyna("Tytani Wejherowo", "Simon")

print(team1.budzet)
print(team1.transfery)

team1.budzet = 10000
print(team1.budzet)

team1.transfery = "Ciupić"
team1.transfery = ["Aginagalde", "Abaloo"]
print(team1.transfery)
