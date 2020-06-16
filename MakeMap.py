import folium
from ClassCar import CarData

# m = folium.Map(location=[36.833972, 127.178548],
#                zoom_start=12)

def Pressed():
    map_osm = folium.Map(location=[37.3402849,126.7313189],zoom_start=15)
    folium.Marker([37.3402849,126.7313189], popup="산기대").add_to(map_osm)
    map_osm.save('Map1.html')

Pressed()
