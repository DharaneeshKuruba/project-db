import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def app():
    st.title("View Hotel Reviews")

    try:
        hotels = requests.get(f"{API_URL}/hotels", timeout=10).json()
    except requests.RequestException:
        st.error("Could not connect to backend. Start FastAPI and try again.")
        return

    hotel_dict = {hotel["name"]: hotel["id"] for hotel in hotels}
    if not hotel_dict:
        st.warning("No hotels available.")
        return

    selected_hotel = st.selectbox("Select Hotel", list(hotel_dict.keys()), key="view_hotel_select")

    if st.button("Show Reviews"):
        hotel_id = hotel_dict[selected_hotel]
        res = requests.get(f"{API_URL}/reviews/{hotel_id}", timeout=10)

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