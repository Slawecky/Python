# Synuś w c
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

startc = int(input("Podaj : "))
startf = int(0)
stopc = int(300)
stopf = int(300)
krok = int(5)

print("\nFahrenheit Celsjusz\n")
while startc <= stopc:
    print(startc, "         ", round((startc-32)*(5/9), 1))
    startc = startc + krok
print("\nCelsjusz Fahrenheit\n ")

while startf <= stopf:
    print(startf, "          ", round((startf*(5/9) + 32), 3))
    startf = startf + krok

# Ślązak
