import requests
from bs4 import BeautifulSoup
import codecs

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}
r = requests.get(
    'https://www.iprogrammatori.it/rss/offerte-di-lavoro.xml', headers=headers)

soup = BeautifulSoup(r.text, 'lxml-xml')

channel = soup.find('channel')
items = channel.find_all('item')

print(items[0].find('title').text)
print(items[0].find('link').text)
print(items[0].find('category').text)
print(items[0].find('pubDate').text)

description = BeautifulSoup(items[0].find('description').text, 'html.parser')

print(codecs.decode(description.get_text(), 'utf-8'))
