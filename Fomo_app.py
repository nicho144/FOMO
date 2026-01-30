# fomo_app.py
import streamlit as st
import pandas as pd

# -----------------------
# Mock backend data
# -----------------------
movement_data = [
    {"id": 1, "lat": -33.8688, "lon": 151.2093, "activity_index": 0.92, "type": "party", "name": "Downtown Rooftop Bar"},
    {"id": 2, "lat": -33.8700, "lon": 151.2070, "activity_index": 0.85, "type": "creative", "name": "City Park Meetup"},
    {"id": 3, "lat": -33.8675, "lon": 151.2060, "activity_index": 0.88, "type": "music", "name": "Live Music Venue"},
    {"id": 4, "lat": -33.8695, "lon": 151.2085, "activity_index": 0.80, "type": "business", "name": "Co-working Cafe"}
]

# -----------------------
# Function to get top hotspots
# -----------------------
def get_top_hotspots(lat, lon, top_n=5):
    # For mock, ignore lat/lon, just sort by activity_index
    sorted_data = sorted(movement_data, key=lambda x: x["activity_index"], reverse=True)
    hotspots = []
    for tile in sorted_data[:top_n]:
        hotspots.append({
            "Name": tile["name"],
            "Latitude": tile["lat"],
            "Longitude": tile["lon"],
            "FOMO Score": round(tile["activity_index"] * 100),
            "Type": tile["type"]
        })
    return hotspots

# -----------------------
# Streamlit App
# -----------------------
st.set_page_config(page_title="FOMO Live Hotspots", layout="wide")
st.title("FOMO — Live Hotspot Finder")

st.markdown("""
Enter your location coordinates below to see the top FOMO hotspots in your area.
""")

# User inputs
lat = st.number_input("Latitude", value=-33.8688, step=0.0001)
lon = st.number_input("Longitude", value=151.2093, step=0.0001)

if st.button("Find Hotspots"):
    hotspots = get_top_hotspots(lat, lon)
    
    # Display as table
    st.subheader("Top Hotspots")
    df = pd.DataFrame(hotspots)
    st.dataframe(df)

    # Display on map
    st.subheader("Map View")
    map_data = pd.DataFrame({
        'lat': [h["Latitude"] for h in hotspots],
        'lon': [h["Longitude"] for h in hotspots],
        'name': [h["Name"] for h in hotspots],
        'fomo': [h["FOMO Score"] for h in hotspots]
    })
    st.map(map_data)
    
    # Simulate GPT-style response
    st.subheader("FOMO AI Summary")
    summary_lines = [f"{i+1}. {h['Name']} — FOMO {h['FOMO Score']} — {h['Type']}" 
                     for i, h in enumerate(hotspots)]
    st.write("\n".join(summary_lines))