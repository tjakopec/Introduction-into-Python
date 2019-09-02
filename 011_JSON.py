import urllib.request, json
from var_dump import var_dump #https://github.com/sha256/python-var-dump

with urllib.request.urlopen("https://vit.hr/GIP/API/10/json/prvaSlovaVelika") as url:
    data = json.loads(url.read().decode())

var_dump(data)

for o in data:
    print(o['ime'] + ' ' + o['prezime'] )
