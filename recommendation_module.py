import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def compute_user_similarity(user_item_matrix):
    user_item_pivot = user_item_matrix.pivot_table(index='user_id', columns='item_id', values='rating', fill_value=0)
    similarity_matrix = cosine_similarity(user_item_pivot)
    similarity_df = pd.DataFrame(similarity_df, index=user_item_pivot.index, columns=user_item_pivot.index)
    return similarity_df

def recommend_items(user_id, user_item_matrix, similarity_df, top_n=3):
    if user_id not in similarity_df.index:
        return ["Sorry, user not found."]
    
    similar_users = similarity_df[user_id].sort_values(ascending=False).drop(user_id).head(top_n).index
    user_ratings = user_item_matrix.set_index('user_id')
    recommended_items = (
        user_item_matrix[user_item_matrix['user_id'].isin(similarity_df.loc[user_id].nlargest(top_n+1).index)]
        .groupby('item_id')['rating']
        .mean()
        .sort_values(ascending=False)
        .head(top_n)
        .index.tolist()
    )
    return recommended_items
