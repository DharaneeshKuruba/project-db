import streamlit as st

# Import your existing pages
import post_review
import view_reviews

st.set_page_config(page_title="Hotel Review App", layout="centered")

st.title("🏨 Hotel Review System")

# Sidebar navigation (acts like routes)
page = st.sidebar.radio("Go to", ["Post Review", "View Reviews"])

# Route handling
if page == "Post Review":
    post_review.app()

elif page == "View Reviews":
    view_reviews.app()