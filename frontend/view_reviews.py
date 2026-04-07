import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("View Hotel Reviews")

# Fetch hotels
hotels = requests.get(f"{API_URL}/hotels").json()
hotel_dict = {hotel["name"]: hotel["id"] for hotel in hotels}

selected_hotel = st.selectbox("Select Hotel", list(hotel_dict.keys()))

if st.button("Show Reviews"):
    hotel_id = hotel_dict[selected_hotel]

    res = requests.get(f"{API_URL}/reviews/{hotel_id}")

    if res.status_code == 200:
        reviews = res.json()

        if not reviews:
            st.warning("No reviews yet")

        for r in reviews:
            st.subheader(f"{r['username']} ⭐ {r['rating']}")
            st.write(r["review"])
            st.divider()
    else:
        st.error("Error fetching reviews")