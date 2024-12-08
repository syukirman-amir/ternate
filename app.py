import streamlit as st
from arcgis.gis import GIS
from arcgis.mapping import WebMap

# Membuat koneksi ke ArcGIS Online (atau Portal)
gis = GIS("home")  # atau bisa menggunakan kredensial ArcGIS Online

# ID Web Map untuk Ternate, pastikan Anda punya ID Web Map yang sudah ada
web_map_id = "abd95acd635d43a097727e908d450b03"  # Gantilah dengan ID Web Map yang sesuai

# Membuat objek WebMap
web_map = WebMap(gis.content.get(web_map_id))

# Menampilkan peta
st.title("Peta Lokasi Ternate")
web_map.show()
