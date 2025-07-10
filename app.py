# app.py

import streamlit as st
from recommender import recommend

st.set_page_config(page_title="🛍️ E-commerce Recommender", page_icon="🛒")

st.title("🛒 E-commerce Product Recommendation System")

st.markdown("""
Welcome!  
Type a product name below and get smart recommendations based on user preferences.

> Example products: `Galaxy S21`, `iPhone 14`, `Redmi Note 12`, `Fire-Boltt Ninja`
""")

# Input field
product_name = st.text_input("🔍 Enter a product name:")

# Button click
if st.button("Get Recommendations"):
    if not product_name:
        st.warning("Please enter a product name.")
    else:
        recommendations = recommend(product_name)

        if isinstance(recommendations, str):
            st.error(recommendations)
        elif len(recommendations) == 0:
            st.warning("😐 Sorry, no relevant recommendations found.")
        else:
            st.success(f"📦 Top Recommendations for '{product_name}':")
            for i, (rec_product, score) in enumerate(recommendations, 1):
                if score == 0.0:
                    st.write(f"{i}. 🛍️ {rec_product}")
                else:
                    st.write(f"{i}. 🛍️ {rec_product} — 🧠 Similarity: {score:.2f}")
            st.info("Explore more products to find your perfect match!")

# Run command : streamlit run app.py

