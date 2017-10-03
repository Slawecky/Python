# Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
#
#   #
#  ###
# #####

# Oryginał

wysokosc = int(input("Podaj wysokość piramidy Mario : "))

print("\nPiramida Mario Bros. w oryginale\n")
for i in range(wysokosc):
    print(" "*(wysokosc-i)+"#"*(i+1))


# W drugą stronę

print("\nPiramida Mario Bros. w drugą stronę\n")
for i in range(wysokosc):
    print("#" * (i * 2 + 1))


# W drugą stronę wyśrodkowana

print("\nPiramida Mario Bros. w drugą stronę wyśrodkowana\n")
for i in range(wysokosc):
    print((wysokosc - 1) * " " + "#" * (i * 2 + 1))

# Z zadania
print("\nPiramida Mario Bros. z zadania\n")
for i in range(wysokosc):
    print(" "*(wysokosc-i)+"#"*(i+1) + "#" * i)
