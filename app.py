import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit.components.v1 import html

# Koordinat pusat Ternate
latitude = -0.7994
longitude = 127.3806

# Membuat peta dasar menggunakan folium
map_ternate = folium.Map(location=[latitude, longitude], zoom_start=12)

# Menambahkan MarkerCluster untuk menampung beberapa marker
marker_cluster = MarkerCluster().add_to(map_ternate)

# Data lokasi-lokasi yang ingin ditampilkan di peta (contoh lokasi kecamatan di Ternate)
locations = [
    {"name": "Kecamatan Ternate Selatan", "lat": -0.7834, "lon": 127.3918},
    {"name": "Kecamatan Ternate Utara", "lat": -0.7905, "lon": 127.3810},
    {"name": "Kecamatan Pulau Ternate", "lat": -0.8100, "lon": 127.3825},
    {"name": "Kecamatan Ternate Tengah", "lat": -0.7944, "lon": 127.3889}
]

# Menambahkan marker untuk setiap lokasi
for location in locations:
    folium.Marker([location["lat"], location["lon"]], popup=location["name"]).add_to(marker_cluster)

# Menampilkan peta dengan Streamlit menggunakan st.components.v1.html
st.title("Peta Interaktif Ternate")
st.write("Peta interaktif menggunakan Folium")

# Mengonversi peta ke HTML dan menampilkannya menggunakan Streamlit
map_html = map_ternate._repr_html_()
html(map_html, height=600)
