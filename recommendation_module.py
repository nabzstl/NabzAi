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

def recommend_items(user_id: str, user_item_matrix: pd.DataFrame, similarity_df: pd.DataFrame) -> list:
    if user_input not in similarity_df.columns:
        return ["No recommendations found (user not in database)."]

    # Continue normally
    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:4].index
    recommended_items = user_item_matrix.loc[similar_users].mean().sort_values(ascending=False).head(3).index.tolist()

    return recommended_items

