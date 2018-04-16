# Import folium
import folium

# create variables for locations
office_loc = [40.766483,-73.0207118]
home_loc = [40.770015, -73.02714]
# put all locations in a list
locations = [office_loc, home_loc]
# set the focal point of the map
map = folium.Map(location=[40.7619066,-73.037737], zoom_start=10, tiles="OpenStreetMap")

# Create a feature group to make code more readable
fg = folium.FeatureGroup(name="My Map")

"""
Add features to the feature group, we can do like below, or we can use 
a for loop which is more efficient especially when there are many items to 
add to the feature group

fg.add_child(folium.Marker(location=office_loc, popup="Office"))
fg.add_child(folium.Marker(location=home_loc, popup="Home"))

map.add_child(fg)
map.save("Map2.html")
"""
# for loop to add coordinates to feature group fg
for location in locations:
    fg.add_child(folium.Marker(location=location))
    map.add_child(fg)

#save the map
map.save("Map3.html")

# Now lets bring data in from a text file since that is how this would normally be done
import pandas as pd
# create a volcanoes variable
volcanoes = pd.read_csv("Volcanoes_USA.txt")
# now lets get the lattitude and longitude into a data frame of one column separated by a ","
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])