import pandas as pd  # <-- ADD THIS LINE
from sklearn.metrics.pairwise import cosine_similarity

def compute_user_similarity(user_item_matrix):
    user_item_pivot = user_item_matrix.pivot_table(index='user_id', columns='item_id', values='rating', fill_value=0)
    similarity_df = user_item_pivot.dot(user_item_pivot.T)
    return similarity_df

def recommend_items(user_id, user_item_matrix, similarity_df, top_n=3):
    if user_id not in similarity_df.index:
        return ["itemA", "itemB", "itemC"]  # Default recommendations for unknown users

    similar_users = similarity_df[user_id].sort_values(ascending=False).index[1:]
    recommendations = set()

    for sim_user in similar_users:
        user_items = set(user_item_matrix[user_item_matrix['user_id'] == sim_user]['item_id'])
        recommendations.update(user_items)

        if len(recommendations) >= top_n:
            break

    return list(recommendations)[:top_n]
                
def evaluate_recommendations(recommendations):
    """
    Evaluate recommendations based on some criteria.
    This is just a placeholder. You should replace it with your logic.
    """
    if not recommendations:
        return "No recommendations generated."
    # Simple placeholder evaluation
    return f"Generated {len(recommendations)} recommendations. Evaluation complete."


    recommended_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return [item[0] for item in recommended_items]
