import requests
r = requests.get('https://www.iprogrammatori.it/rss/offerte-di-lavoro.xml')

print(r.status_code)
