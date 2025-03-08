import pandas as pd
from data_module import load_data
from recommendation_module import compute_user_similarity, recommend_items
from evaluation_module import evaluate_recommendations
from self_improvement_module import adapt_recommendation_strategy
from retraining_module import retrain_model, load_model
from logging_module import log_performance
from safety_module import filter_recommendations
from ethical_module import enforce_ethics
from resource_module import resource_report
import firebase_module

def main():
    # Initialize Firebase
    firebase_module.initialize_firebase()

    user_item_matrix = load_data()

    similarity_df = load_model()
    if similarity_df is None:
        similarity_df = retrain_model(user_item_matrix, compute_user_similarity)

    user_id = 1
    top_n = 2

    # Fetch real-time feedback from Firebase
    user_feedback_history = firebase_module.get_user_feedback(user_id)

    # If there's no feedback yet, use default data
    if user_feedback_history is None:
        user_feedback_history = [
            {'C': 5, 'D': 4},
            {'C': 2, 'D': 2},
            {'C': 4, 'D': 5}
        ]
    else:
        user_feedback_history = list(user_feedback_history.values())

    for i, user_feedback in enumerate(user_feedback_history):
        recommended = recommend_items(user_id, user_item_matrix, similarity_df, top_n)

        # Apply safety controls
        recommended = filter_recommendations(recommended)

        # Apply ethical constraints
        recommended = enforce_ethics(recommended)

        evaluation_score = evaluate_recommendations(recommended, user_feedback)

        # Logging performance and resources
        resources = resource_report()
        log_performance(i+1, user_id, recommended, evaluation_score, top_n)

        print(f"Cycle {i+1} - Recommended: {recommended}, Score: {evaluation_score}, {resources}")

        top_n = adapt_recommendation_strategy(evaluation_score, top_n)

        # Save current cycle feedback back to Firebase
        firebase_module.save_user_feedback(user_id, user_feedback)

        # Retrain model after feedback
        similarity_df = retrain_model(user_item_matrix, compute_user_similarity)

if __name__ == "__main__":
    main()
