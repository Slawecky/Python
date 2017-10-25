# https://xkcd.com/json.html
import requests
import json

url = "http://xkcd.com/info.0.json"
response = requests.get(url)
response.raise_for_status()

json_info = json.load(response.text)

print(json.dumps(json_info, indent=4))