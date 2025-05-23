import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium

# Функція для отримання координат
@st.cache_data
def get_coordinates(place_name):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.geocode(place_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# Вступ
st.title("Лабораторна робота 22: Folium + Streamlit")
st.markdown("Це інтерактивна карта з районами Івано-Франківської області.")

# Вибір районів та категорій
districts = ["Івано-Франківський район", "Калуський район", "Коломийський район", "Надвірнянський район"]
selected_districts = st.multiselect("Оберіть райони для відображення", districts, default=districts)

categories = ["A", "B", "C", "D"]
colors = {"A": "red", "B": "green", "C": "pink", "D": "blue"}

# Випадковий вибір категорії для району (або можна реалізувати ручний вибір)
import random
district_categories = {district: random.choice(categories) for district in selected_districts}

# Створення карти
m = folium.Map(location=[48.9226, 24.7103], zoom_start=8)

# Додавання FeatureGroup по категоріях
catD = {c: folium.FeatureGroup(c).add_to(m) for c in categories}
folium.LayerControl().add_to(m)

# Додавання маркерів
for district, cat in district_categories.items():
    coords = get_coordinates(district)
    if coords:
        folium.Marker(
            location=coords,
            popup=f"{district} ({cat})",
            icon=folium.Icon(color=colors[cat])
        ).add_to(catD[cat])

# Відображення карти у Streamlit
st_folium(m, width=725)
