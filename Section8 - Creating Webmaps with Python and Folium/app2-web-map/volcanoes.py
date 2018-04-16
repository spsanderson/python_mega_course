import folium
import pandas as pd

# in the real world we will have many locations to plot
# most likely in text/json etc
data = pd.read_csv("Volcanoes_USA.txt")
# make a list of lattitude and longitude that we will zip() later in script
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
volname = list(data["NAME"])

# create base map
map = folium.Map(location=[38.58, -99.09], zoom_start=5)
# create feature group
fg = folium.FeatureGroup(name="My Map of Volcanoes in USA")
# loop through lat and lon, use zip()
for lt, ln, el, nm in zip(lat, lon, elev, volname):
    fg.add_child(folium.Marker(location=([lt, ln])
    , popup = folium.Popup(
        "Elevation: " + str(el) + "m - Name: " + str(nm), parse_html=True
        )
    )
)
    map.add_child(fg)
map.save("USA_Volcanoes.html")
# save map as html file
"""
for some reason the below does not work even though it was noted it did for some here:
https://github.com/python-visualization/folium/issues/469

# try formatting popup with .format
for lt, ln, el, nm in zip(lat, lon, elev, volname):
    fg.add_child(folium.Marker(location=[lat, lon])),
    popup = (
        "Elevation: {elev}</br>"
        "Name: {volname}<br>"
    ).format(elev=str(el), volname=str(nm))
    map.add_child(fg)
map.save("USA_Volcanoes_b.html")

"""
