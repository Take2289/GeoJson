import geojson 
from matplotlib import pyplot as plt
import requests 

req = requests.get ("https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/35/query?where=1%3D1&outFields=BLOCK,LATITUDE,LONGITUDE,START_DATE,END_DATE,REPORT_DAT&outSR=4326&f=json")
Geodata_json = req.json()

d = geojson.dumps(Geodata_json, indent=2)

order = [1,2,3,4,5,6,7,8,9,10]
info = [10,20,30,40,50,60,70,80,90,100]

i = plt.plot(info, order) 
plt.show()

s = str(i) 

x = (s + d)


f = open('Geo.shp', 'w')
f.write(x)
f.close()

Shape =(x)


print(Shape) 


