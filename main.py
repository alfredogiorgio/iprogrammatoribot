import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}
r = requests.get(
    'https://www.iprogrammatori.it/rss/offerte-di-lavoro.xml', headers=headers)

print(r.text)
