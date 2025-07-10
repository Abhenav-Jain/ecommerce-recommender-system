# recommender.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset (update your path)
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\Coding\Projects\Project ML\ecom2.csv")

# Pivot table
pivot = df.pivot_table(index='user_id', columns='product_name', values='rating')
pivot.fillna(0, inplace=True)

# Cosine similarity
product_similarity = cosine_similarity(pivot.T)
similarity_df = pd.DataFrame(product_similarity, index=pivot.columns, columns=pivot.columns)

# Recommendation function
def recommend(product_name, top_n=5):
    if product_name not in similarity_df.columns:
        return f"❌ '{product_name}' not found in product list."
    
    # Sort similar products by score (including 0.0)
    similar_scores = similarity_df[product_name].sort_values(ascending=False)

    # Remove the input product itself
    similar_scores = similar_scores.drop(labels=[product_name])

    # Take top N (even if 0.0 similarity)
    top_similar = similar_scores.head(top_n)

    # Return as list of (product_name, similarity_score)
    return list(zip(top_similar.index, top_similar.values))
