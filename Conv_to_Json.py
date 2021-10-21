import json

with open ('Geo.shp') as json_file:
    data = json.load(json_file)


print (data)