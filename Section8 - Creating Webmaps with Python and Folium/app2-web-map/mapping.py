import folium
office_loc = [40.766483,-73.0207118]
home_loc = [40.770015, -73.02714]
map = folium.Map(location=[40.7619066,-73.037737], zoom_start=10, tiles="OpenStreetMap")

# Create a feature group to make code more readable
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=office_loc, popup="Office"))
fg.add_child(folium.Marker(location=home_loc, popup="Home"))
map.add_child(fg)
map.save("Map1.html")

#map.add_child(folium.Marker(location=office_loc, popup="Hi I'm an icon", icon=folium.Icon(color='blue')))
#folium.Marker(home_loc,office_loc,popup="My Office").add_to(map)
#folium.Marker(home_loc,popup="Home").add_to(map)

#map.save("Map2.html")