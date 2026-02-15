"""import cowsay
import sys

if len(sys.argv)==2:
    cowsay.trex("hello,"+ sys.argv[1])
"""

#Resquest library
import json
import requests
import sys

if len(sys.argv)!=2:
    sys.exit()

response= requests.get("https://itunes.apple.com/search?entity=song&limit=1000 &term="+ sys.argv[1])
#print(json.dumps(response.json(),indent=2))


o = response.json()
i=1
for result in o["results"]:
    print(i,result["trackName"])
    i=i+1