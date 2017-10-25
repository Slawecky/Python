import requests

def pobierz_foto(link, sciezka):

    response = requests.get(link)
    if response.status_code == 200:
        bajty = 0

        try:
            with open(sciezka, 'wb') as plik :
                for part in response.iter_content(100000):
                    ilosc = plik.write(part)
                    bajty += ilosc
        except FileNotFoundError:
            bajty = 999999

            # tutaj tworzymy foldery
    #print(f"Zapisano {bajty} bajtów")

def main():
    link = "https://vigilantcitizen.com/wp-content/uploads/2012/12/leadbaphomet1.jpg"
    pobierz_foto(link, "baphomet.jpg")
    if __name__ == "__main__":
        main()
