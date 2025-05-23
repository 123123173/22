import streamlit as st
import folium
from streamlit_folium import st_folium

# СТАБІЛЬНІ координати районів (щоб не викликати geopy і не створювати запити)
district_coords = {
    "Івано-Франківський район": (48.9226, 24.7103),
    "Калуський район": (49.0141, 24.3734),
    "Коломийський район": (48.5300, 25.0400),
    "Надвірнянський район": (48.6330, 24.5697),
}

# Вступ
st.title("Лабораторна робота 22: Folium + Streamlit")
st.markdown("Це інтерактивна карта з районами Івано-Франківської області.")

# Вибір районів
districts = list(district_coords.keys())
selected_districts = st.multiselect("Оберіть райони для відображення", districts, default=districts)

# Категорії та кольори
categories = ["A", "B", "C", "D"]
colors = {"A": "red", "B": "green", "C": "pink", "D": "blue"}

import random
district_categories = {district: random.choice(categories) for district in selected_districts}

# Створення карти
m = folium.Map(location=[48.9226, 24.7103], zoom_start=8)

# Додавання FeatureGroup по категоріях
catD = {c: folium.FeatureGroup(c).add_to(m) for c in categories}
folium.LayerControl().add_to(m)

# Додавання маркерів
for district, cat in district_categories.items():
    coords = district_coords.get(district)
    if coords:
        folium.Marker(
            location=coords,
            popup=f"{district} ({cat})",
            icon=folium.Icon(color=colors[cat])
        ).add_to(catD[cat])

# Відображення карти у Streamlit
st_folium(m, width=725)
