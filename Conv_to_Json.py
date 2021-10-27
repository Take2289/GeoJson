import geojson

with open ('Geo.shp') as json_file:
    data = geojson.load(json_file)


print (data)
