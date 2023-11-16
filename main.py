from bs4 import BeautifulSoup
import json
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import aiohttp


async def scrape():

    print("andato")
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.iprogrammatori.it/rss/offerte-lavoro-crawler.xml', headers=headers) as resp:
            r = await resp.text()

    soup = BeautifulSoup(r.text, 'lxml-xml')

    jobs = soup.find_all('job')

    f = open('jobs.json')
    data = json.load(f)

    size = len(data)

    for job in jobs:
        jobJson = {}

        jobJson['id'] = job.find('id').text
        jobJson['title'] = job.find('title').text
        jobJson['url'] = job.find('url').text
        jobJson['content'] = job.find('content').text.encode(
            'iso-8859-1').decode('utf-8', errors='ignore')

        try:
            jobJson['city'] = job.find('city').text
        except:
            jobJson['city'] = "Non specificato"

        try:
            jobJson['company'] = job.find('company').text
        except:
            jobJson['company'] = "Non specificato"

        try:
            jobJson['requirements'] = job.find('requirements').text
        except:
            jobJson['requirements'] = "Non specificato"

        try:
            jobJson['date'] = job.find('date').text.encode(
                'iso-8859-1').decode('utf-8', errors='ignore')
        except:
            jobJson['date'] = "Non specificato"

        try:
            jobJson['jobtype'] = job.find('jobtype').text
        except:
            jobJson['jobtype'] = "Non specificato"

        data.append(jobJson)

        print(jobJson['title'])

    with open('jobs.json', 'w') as file:
        json.dump(data, file, indent=4)

sched = AsyncIOScheduler()
sched.add_job(scrape, 'interval', minutes=1)
sched.start()
