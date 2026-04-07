import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Post Hotel Review")

# Fetch hotels
hotels = requests.get(f"{API_URL}/hotels").json()
hotel_dict = {hotel["name"]: hotel["id"] for hotel in hotels}

selected_hotel = st.selectbox("Select Hotel", list(hotel_dict.keys()))

username = st.text_input("Enter your name")

rating = st.slider("Rating", 1, 5)

review = st.text_area("Write your review")

if st.button("Submit Review"):
    payload = {
        "hotel_id": hotel_dict[selected_hotel],
        "username": username,
        "rating": rating,
        "review": review
    }

    res = requests.post(f"{API_URL}/review", json=payload)

    if res.status_code == 200:
        st.success("Review submitted!")
    else:
        st.error("Error submitting review")