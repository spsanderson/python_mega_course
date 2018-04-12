import folium

map = folium.Map(location=[40.766483,-73.0207118], zoom_start=10, tiles="Mapbox Bright")
map.save("Map1.html")