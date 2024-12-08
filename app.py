import streamlit as st
import folium
from folium.plugins import MarkerCluster

# Koordinat Ternate
latitude = -0.7994
longitude = 127.3806

# Membuat peta dasar
map_ternate = folium.Map(location=[latitude, longitude], zoom_start=12)

# Menambahkan marker untuk lokasi tertentu
marker_cluster = MarkerCluster().add_to(map_ternate)
folium.Marker([latitude, longitude], popup="Ternate").add_to(marker_cluster)

# Menampilkan peta dalam Streamlit
st.title("Peta Interaktif Ternate")
st.write("Peta dengan folium:")
st.markdown(folium.Figure().add_child(map_ternate)._repr_html_(), unsafe_allow_html=True)
