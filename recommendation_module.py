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

def recommend_items(user_id, user_item_matrix, similarity_df, top_n=3):
    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:]
    recommendations = user_item_matrix.loc[similar_users.index].mean().sort_values(ascending=False)
    recommended_items = recommendations.head(top_n).index.tolist()
    return recommended_items
