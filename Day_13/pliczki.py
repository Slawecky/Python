import shutil, os, send2trash

print(shutil.disk_usage('.'))

print("\nJestem w : ")
print(os.getcwd())

#os.mkdir(".moj_folder")

#shutil.copytree("/home/slawecky/GIT/Python", "/home/slawecky/GIT/Python_COP")

#os.rmdir(".moj_folder")

for ele in os.listdir():
    print(ele)

print(os.listdir())

for biezacy_folder, podfoldery, pliki in os.walk("../"):
    print(f"Obecny folder : {biezacy_folder}")
    for pofolder in  podfoldery:
        print(f"odfolder {pofolder}) wew. {biezacy_folder}")
    for plik in pliki:
        print(os.path.abspath(plik))
        #print(f"Plik {plik} wew. folderu {biezacy_folder}")
