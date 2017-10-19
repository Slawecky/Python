# program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
# użyć continue

start = 0
koniec = 20

while start <= koniec:
    if start %4 == 0:
        print(f"{start} jest podzielna przez 4")
    else:
        print(f"{start} nie jest podzielna przez 4")
    start +=1
start = 0
while start <= koniec:
    if start %4 == 0:
        print(f"{start} jest podzielna przez 4")
    start += 1
    continue