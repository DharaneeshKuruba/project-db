import streamlit as st

st.set_page_config(page_title="Hotel Review App", layout="centered")

# Import pages only after configuring Streamlit page settings.
import post_review
import view_reviews

st.title("🏨 Hotel Review System")

# Sidebar navigation (acts like routes)
page = st.sidebar.radio("Go to", ["Post Review", "View Reviews"])

# Route handling
if page == "Post Review":
    post_review.app()

elif page == "View Reviews":
    view_reviews.app()