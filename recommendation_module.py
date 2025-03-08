import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def compute_user_similarity(user_item_matrix: pd.DataFrame) -> pd.DataFrame:
    similarity_matrix = cosine_similarity(user_item_matrix)
    similarity_df = pd.DataFrame(
        similarity_matrix,
        index=user_item_matrix.index,
        columns=user_item_matrix.index
    )
    return similarity_df

def recommend_items(user_input: str, user_item_matrix: pd.DataFrame, similarity_df: pd.DataFrame) -> list:
    if user_input not in similarity_df.columns:
        return ["User not found, please enter a valid username."]
    
    # Get most similar users
    similar_users = similarity_df[user_input].sort_values(ascending=False)[1:]
    
    # Get items user has not rated yet
    items_user_has = set(user_item_matrix.loc[user_input].dropna().index)
    recommendations = {}

    # Recommend items based on similar users' preferences
    for similar_user in similar_users.index:
        items = user_item_matrix.loc[similar_users.index].loc[similar_users > 0].mean(axis=0)
        recommended_items = items.sort_values(ascending=False).index
        for item in recommended_items:
            if item not in user_item_matrix.columns[user_item_matrix.loc[user_input].notnull()]:
                return recommended_items[:3].tolist()

    return ["No recommendations available."]
