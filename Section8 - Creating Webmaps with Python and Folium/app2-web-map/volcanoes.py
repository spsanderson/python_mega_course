# import libraries
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
# create base zoom location
base_loc = [38.58, -99.09]
# lets make a function to color the map markers based on elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'blue'
    else:
        return 'red'

# create base map
map = folium.Map(location = base_loc, zoom_start = 5)

# create feature group for population
fg_pop = folium.FeatureGroup(name="Population")
# lets add a layer to the map it will be a geojson file
fg_pop.add_child(
    folium.GeoJson(
        data = open('world.json','r', encoding='utf-8-sig').read(),
        # Styling based on population size in geoJson file ['properties']['POP2005']
        style_function = lambda x: {
            'fillColor':'green' if x['properties']['POP2005'] < 10000000 
            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
            else 'red'
            }
        )
    )

# create feature group for volcanoes
fg_vol = folium.FeatureGroup(name="Volcanoes")
# loop through lat and lon, use zip()
for lt, ln, el, nm in zip(lat, lon, elev, volname):
    fg_vol.add_child(
        folium.CircleMarker(
            location=([lt, ln])
            , popup = folium.Popup(
                "Elevation: " + str(el) + "m - Name: " + str(nm), parse_html=True
            )
            , color = color_producer(el)
            , radius = 6
            , fill = True
            , fill_color = color_producer(el)
            , fill_opacity = 0.618
        )
    )

# add feature groups to map
map.add_child(fg_pop)
map.add_child(fg_vol)

# add layer control
map.add_child(
    folium.LayerControl()
)

# save map as html file
map.save("USA_Volcanoes.html")

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
