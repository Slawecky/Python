zakres = range(23, 45463)
il_niepa = 0
il_pa = 0

for i in zakres:
    if i % 2 == 0:
        il_pa += 1
    else:
        il_niepa += 1
print(f"Nieparzyste {il_niepa}, parzyste {il_pa}")
