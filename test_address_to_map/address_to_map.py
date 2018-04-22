# import libraries
import pandas as pd
import geopy as geo
import folium as folium
import math as math

# import data from csv file
data = pd.read_csv('test_loc.csv')
data = data[1:400]

# set a nominatum helper
nom = geo.Nominatim(timeout=100)

"""
found this at https://gis.stackexchange.com/questions/173569/avoid-time-out-error-nominatim-geopy-open-street-maps
not sure how to implement it though

def do_geocode(address):
    try:
        return nom.geocode(address)
    except geo.exc.GeocoderTimedOut:
        return do_geocode(address)
"""

# use nom.geocode() to get coordinates
data["coordinates"] = data["PT_FULL_ADDRESS"].apply(nom.geocode)

# make latitude and longitude columns that will get zipped later
data["latitude"] = data["coordinates"].apply(lambda x: x.latitude if x != None else None)
data["longitude"] = data["coordinates"].apply(lambda x: x.longitude if x != None else None)

# make a list of lattitude and longitude that we will zip() later in script
lat = list(data["latitude"])
lon = list(data["longitude"])
address = list(data["PT_FULL_ADDRESS"])

# create base zoom location
base_loc = [40.779675,-72.9811633]

# create base map
map = folium.Map(location = base_loc, zoom_start = 10)

# create feature group for population
fg_add = folium.FeatureGroup(name="Address")

# loop through lat and lon, use zip()
for lt, ln, a in zip(lat, lon, address):
    if math.isnan(lt) or math.isnan(ln):
        print("Skipping latitude and longitude as one or both are NaN")
    else:
        fg_add.add_child(
            folium.CircleMarker(
                location=([lt, ln])
                , popup = folium.Popup(
                    "Address: " + str(a), parse_html=True
                )
                , color = 'blue'
                , radius = 3
                , fill = True
                , fill_color = 'blue'
                , fill_opacity = 0.618
            )
        )
        
# create feature group for base location
fg_hosp = folium.FeatureGroup(name="Hospital")
fg_hosp.add_child(
    folium.Marker(
        location=base_loc
        , popup="BMHMC"
        , icon = folium.Icon(color='red')
        )
    )

# add feature groups to map
map.add_child(fg_add)
map.add_child(fg_hosp)

# add layer control
map.add_child(
    folium.LayerControl()
)

# save map as html file
map.save("test_map.html")