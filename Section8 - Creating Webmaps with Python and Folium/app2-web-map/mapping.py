import folium
office_loc = [40.766483,-73.0207118]
home_loc = [40.770015, -73.02714]
map = folium.Map(location=[40.7619066,-73.037737], zoom_start=10, tiles="OpenStreetMap")

# Create a feature group to make code more readable
fg = folium.FeatureGroup(name="My Map")
# add features
fg.add_child(folium.Marker(location=office_loc, popup="Office"))
fg.add_child(folium.Marker(location=home_loc, popup="Home"))
# add features to the map
map.add_child(fg)
#save the map
map.save("Map1.html")