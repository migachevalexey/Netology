import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten, kmeans2
import pprint

def call_api(uri, result_key):
    json = {}
    try:
        json = requests.get(uri, headers = { 'X-Auth-Token': '402a9674e0c940fd9eb03d1150263ba9' }).json()
        return json[result_key]
    except:
        print(json)
        return None
teams = call_api('http://api.football-data.org/v1/soccerseasons/439/teams', 'teams')

for team in teams:
    players = call_api(team['_links']['players']['href'], 'players')
    fixtures = call_api(team['_links']['fixtures']['href'], 'fixtures')
    pprint.pprint(fixtures)


# for i in teams:
#     print(i['name'])
# pprint.pprint(teams)