import pandas as pd  # <-- ADD THIS LINE
from sklearn.metrics.pairwise import cosine_similarity

def compute_user_similarity(user_item_matrix):
    similarity = cosine_similarity(user_item_matrix)
    return pd.DataFrame(similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def recommend_items(user_id, user_item_matrix, similarity_df, top_n=2):
    similar_users = similarity_df[user_id].sort_values(ascending=False).index[1:]
    user_items = set(user_item_matrix.columns[user_item_matrix.loc[user_id] > 0])

    recommendations = {}
    for sim_user in similar_users:
        sim_user_items = user_item_matrix.columns[user_item_matrix.loc[sim_user] > 0]
        for item in sim_user_items:
            if item not in user_items:
                recommendations[item] = recommendations.get(item, 0) + similarity_df.loc[user_id, sim_user]

    recommended_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return [item[0] for item in recommended_items]
