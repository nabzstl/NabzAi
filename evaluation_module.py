def evaluate_recommendations(recommended_items, user_feedback):
    feedback_scores = [user_feedback.get(item, 0) for item in recommended_items]
    return sum(feedback_scores) / len(recommended_items) if feedback_scores else 0
