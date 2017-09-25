menu = {}
menu['1']="Dodaj studenta"
menu['2']="Usuń studenta"
menu['3']="Wyszukaj studenta"
menu['4']="Pokaż listę studentów "
menu['9']="Zakończ program"

while True:
  #options=menu.keys()
  wybor=menu.keys()
  #options.sort()
  #wybor.sort_keys()

for inp in wybor:
    print(wybor, menu[inp])

    selection=raw_input("Please Select:")
    if selection =='1':
      print("add")
    elif selection == '2':
      print("delete")
    elif selection == '3':
      print("find")
    elif selection == '4':
      break
    else:
      print("Unknown Option Selected!")
