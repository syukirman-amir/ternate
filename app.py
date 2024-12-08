import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit.components.v1 import html

# Data koordinat untuk beberapa kelurahan di Ternate
kelurahan_data = [
    {"kelurahan": "Kelurahan Ternate Barat", "lat": -0.7942, "lon": 127.3796},
    {"kelurahan": "Kelurahan Ternate Timur", "lat": -0.7846, "lon": 127.3943},
    {"kelurahan": "Kelurahan Kota Baru", "lat": -0.7930, "lon": 127.3780},
    {"kelurahan": "Kelurahan Kampung Durian", "lat": -0.7955, "lon": 127.3815},
    {"kelurahan": "Kelurahan Gamalama", "lat": -0.8042, "lon": 127.3875},
    {"kelurahan": "Kelurahan Mayau", "lat": -0.7969, "lon": 127.3699}
]

# Membuat peta dasar dengan folium, berpusat di Ternate
map_ternate = folium.Map(location=[-0.7994, 127.3806], zoom_start=12, tiles='stamenterrain')

# Menambahkan MarkerCluster untuk menampung beberapa marker
marker_cluster = MarkerCluster().add_to(map_ternate)

# Menambahkan marker untuk setiap kelurahan
for kelurahan in kelurahan_data:
    folium.Marker(
        [kelurahan["lat"], kelurahan["lon"]],
        popup=f"<strong>{kelurahan['kelurahan']}</strong><br>Latitude: {kelurahan['lat']}<br>Longitude: {kelurahan['lon']}"
    ).add_to(marker_cluster)

# Menampilkan peta dengan Streamlit menggunakan st.components.v1.html
st.title("Peta Interaktif Kelurahan Ternate")
st.write("Peta ini menampilkan lokasi kelurahan-kelurahan di Ternate.")

# Mengonversi peta ke HTML dan menampilkannya menggunakan Streamlit
map_html = map_ternate._repr_html_()
html(map_html, height=600)
