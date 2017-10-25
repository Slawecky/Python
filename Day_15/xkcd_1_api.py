# https://xkcd.com/json.html
import requests
import json
from pprint import PrettyPrinter
import os
from Day_14.download import pobierz_foto

pattern = "http://xkcd.com/{i}/info.0.json"

def get_current_comic():
    response = requests.get("http://xkcd.com/info.0.json")
    json_info = json.loads(response.text)
    return json_info

def comic_link(url):
    response = requests.get(url)
    return json.loads(response.text)['img']

def main():
    #czytelne wydruk
    pp = PrettyPrinter(4)
    xkcd_last = get_current_comic()
    pp.pprint(xkcd_last)
    last_comic_num = xkcd_last['num']
    print(last_comic_num)
    os.mkdir('xkcd_comics')

    for x in range(1, 30):
        pic_link = comic_link(pattern.format(i=x))
        pic_path = f"./xkcd_comics/xkcd_{x}"
        pobierz_foto(pic_link,pic_path)
        print(f"Zapisałem foto nr {x}")

if __name__== '__main__':
    main()

