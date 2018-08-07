import requests

url = 'http://steamspy.com/api.php?request=tag&tag=bowling'

json = requests.get(url).json()

app = json['12210']['name']
for i in json:
    print(i)
