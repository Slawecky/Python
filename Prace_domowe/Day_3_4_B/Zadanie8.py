# sprawdz czy litera jest samogłoska czy spolgloska
# if

litera = input(" Podaj literę : ")
samogloski = ("a", "e", "y", "i", "o", "ą", "ę")

if (litera in samogloski):
    print(f"Litera : {litera} jest samogłoską")
else:
    print(f"Litera : {litera} jest spółgłoską")
