import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def app():
    st.title("Post Hotel Review")

    try:
        hotels = requests.get(f"{API_URL}/hotels", timeout=10).json()
    except requests.RequestException:
        st.error("Could not connect to backend. Start FastAPI and try again.")
        return

    hotel_dict = {hotel["name"]: hotel["id"] for hotel in hotels}
    if not hotel_dict:
        st.warning("No hotels available.")
        return

    selected_hotel = st.selectbox("Select Hotel", list(hotel_dict.keys()), key="post_hotel_select")
    username = st.text_input("Enter your name")
    rating = st.slider("Rating", 1, 5)
    review = st.text_area("Write your review")

    if st.button("Submit Review"):
        payload = {
            "hotel_id": hotel_dict[selected_hotel],
            "username": username,
            "rating": rating,
            "review": review,
        }

        res = requests.post(f"{API_URL}/reviews", json=payload, timeout=10)

        if res.status_code == 200:
            st.success("Review submitted!")
        else:
            st.error("Error submitting review")