import streamlit as st
from scripts.recommend import recommend
import pandas as pd

st.set_page_config(page_title="Swiggy Restaurant Recommender", layout="centered")

st.title("🍽️ Swiggy Restaurant Recommendation System")

st.write("Select your preferences to get restaurant recommendations")

# Load cleaned data to get available cities & cuisines
df = pd.read_csv("data/cleaned_data.csv")

cities = sorted(df["city"].unique())
cuisines = sorted(df["cuisine"].str.split(",").explode().unique())

city = st.selectbox("Select City", cities)
cuisine = st.selectbox("Select Cuisine", cuisines)
max_cost = st.slider("Maximum Budget (₹)", 50, 1000, 300)
min_rating = st.slider("Minimum Rating", 1.0, 5.0, 4.0)

if st.button("Get Recommendations"):
    results = recommend(city, cuisine, max_cost, min_rating)

    if results.empty:
        st.warning("No restaurants found for this combination.")
    else:
        st.dataframe(results)
