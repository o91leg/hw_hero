import requests

from pprint import pprint

ids = list()
hero = {}

def find_id(*name):
    for n in name:
        url = 'https://superheroapi.com/api/2619421814940190/search/{}'
        req = requests.get(url.format(n))
        hero.update(req.json())
        for x in hero['results']:
            for k, v in x.items():
                if v == n:
                    ids.append(x['id'])
    return ids


def most_intelligence(ids):
    for v in ids:
        intelligence = list()
        url = 'https://superheroapi.com/api/2619421814940190/{}/powerstats'
        req = requests.get(url.format(v))
        intelligence.append(req.json()['intelligence'])
    for i, item in enumerate(intelligence):
        intelligence[i] = int(item)
        max_intelligence = max(intelligence)
        if str(max_intelligence) == req.json()['intelligence']:
            print('Самый высокий интелект у:', req.json()['name'])


find_id('Hulk', 'Captain America', 'Thanos')

most_intelligence(ids)