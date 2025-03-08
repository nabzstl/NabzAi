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

def recommend_items(user_id: str, user_item_matrix: pd.DataFrame, similarity_df: pd.DataFrame, num_recommendations: int = 5):
    if user_id not in similarity_df.columns:
        raise KeyError(f"User ID {user_id} not found in similarity matrix.")

    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:]
    most_similar_user = similar_users.index[0]

    recommended_items = user_item_matrix.loc[most_similar_user]
    recommended_items = recommended_items[recommended_items > 0].index.tolist()

    return recommended_items[:num_recommendations]
