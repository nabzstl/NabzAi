import numpy as np
import pandas as pd

# Mock dataset: users' ratings of items
data = {
    'user_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    'item_id': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'D', 'C', 'D'],
    'rating': [5, 3, 4, 2, 2, 5, 4, 3, 5, 4]
}

df = pd.DataFrame(data)

# Create a user-item matrix
user_item_matrix = df.pivot_table(index='user_id', columns='item_id', values='rating').fillna(0)

# Compute similarity between users (cosine similarity)
from sklearn.metrics.pairwise import cosine_similarity

user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Simple recommendation function
def recommend_items(user_id, user_item_matrix, similarity_df, top_n=2):
    # Get similar users sorted by similarity score
    similar_users = similarity_df[user_id].sort_values(ascending=False).index[1:]

    # Items rated by the target user
    user_items = set(user_item_matrix.columns[user_item_matrix.loc[user_id] > 0])

    recommendations = {}
    for sim_user in similar_users:
        sim_user_items = user_item_matrix.columns[user_item_matrix.loc[sim_user] > 0]
        for item in sim_user_items:
            if item not in user_items:
                recommendations[item] = recommendations.get(item, 0) + similarity_df.loc[user_id, sim_user]

    # Sort recommendations by score and pick top N
    recommended_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return [item[0] for item in recommended_items]

# Test the recommendation function
user_id = 1
recommended = recommend_items(user_id, user_item_matrix, user_similarity_df, top_n=2)
print(f"Recommended items for user {user_id}: {recommended}")
