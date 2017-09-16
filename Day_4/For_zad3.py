import string

litery = 0
male_litery = 0
duze_litery = 0
cyfry = 0

zdanie = input("Napisz cokolwiek :")

for c in zdanie:
    if c.isdigit():
        cyfry =+1
    elif c.isalpha():
        litery += 1
        if c in string.ascii_lowercase:
            male_litery += 1
        else:
            duze_litery += 1
print(" Litery : ", litery)
print(" Małe litery : ", male_litery)
print(" Duże litery : ", duze_litery)
print(" Cyfry : ",  cyfry)