import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def compute_user_similarity(user_item_pivot: pd.DataFrame) -> pd.DataFrame:
    similarity_matrix = cosine_similarity(user_item_pivot)
    similarity_df = pd.DataFrame(
        similarity_matrix,
        index=user_item_pivot.index,
        columns=user_item_pivot.index
    )
    return similarity_df

def recommend_items(user_id, user_item_matrix, similarity_df, num_recommendations=5):
    if user_id in similarity_df.columns:
        similar_users = similarity_df[user_id].sort_values(ascending=False)[1:]
        most_similar_user = similar_users.index[0]
        recommended_items = user_item_matrix.loc[most_similar_user]
        recommended_items = recommended_items[recommended_items > 0].index.tolist()
    else:
        # User not found, fallback strategy:
        # recommend top popular items or random items
        item_popularity = user_item_matrix.sum().sort_values(ascending=False)
        recommended_items = item_popularity.index.tolist()

    return recommended_items[:num_recommendations]
