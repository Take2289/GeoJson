import json 

import requests

req = requests.get("https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/35/query?where=1%3D1&outFields=CCN,METHOD,BLOCK,DISTRICT,CENSUS_TRACT,LATITUDE,LONGITUDE,START_DATE,END_DATE,REPORT_DAT&outSR=4326&f=json")
Geodata_json = req.json()

Geodata_str = json.dumps(Geodata_json, indent=2)

f = open ('Geo.shp','w')
f.write(Geodata_str)
f.close()


Shape = (f,Geodata_str)

print(Shape)

