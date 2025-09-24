# import required packages
import pandas as pd
import requests
import json


url = "https://mmaapi.p.rapidapi.com/api/mma/event/11243946/statistics"

headers = {
	"x-rapidapi-key": "6f449ecd93mshec15e82a8cac625p1f12f6jsn5fc072a00ce2",
	"x-rapidapi-host": "mmaapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

data = response.json()

with open('data/event_statistics.json', 'w') as f:
    json.dump(data, f, indent=4)


