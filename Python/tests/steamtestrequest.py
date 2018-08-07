import requests
import re

url = 'https://store.steampowered.com/api/appdetails/?appids=8600'

json = requests.get(url).json()
##print(json)
req = json['8600']['data']['pc_requirements']['minimum']
rec = re.search(r'Recommended(.*)', req)
print(rec.group())
#subSpecs = re.sub(r'<([^>]*)>', '', app)
##for i in json:
##    print(i)
## https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key=9D6D1345FF319CE5765E889D05953EA4&language=en_us
