import folium
loc = [40.766483,-73.0207118]
map = folium.Map(location=loc, zoom_start=10, tiles="OpenStreetMap")
map.save("Map1.html")
folium.Marker(loc,popup="My Office").add_to(map)
map.save("Map2.html")