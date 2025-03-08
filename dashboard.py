import streamlit as st
import pandas as pd
from recommendation_module import recommend_items, evaluate_recommendations
from self_improvement_module import adapt_recommendation_strategy
import firebase_module
from firebase_module import get_user_feedback, save_user_feedback
from data_loader import load_data

# Initialize Firebase
firebase_module.initialize_firebase()

# Load data
user_item_matrix, similarity_df = load_data()

# User authentication or selection
user_id = st.text_input('Enter User ID:')

# User chat interface
feedback = st.chat_input("Share your feedback:")
if feedback:
    save_user_feedback(user_id, feedback)
    st.chat_message("user").write(feedback)

# Display feedback history
feedback_history = get_user_feedback(user_id)
if feedback_history := feedback_history:
    for entry in feedback_history:
        st.chat_message("user").write(entry)

# Generate recommendations
recommendations = recommend_items(user_id, user_item_matrix, similarity_df)
st.write("Recommended items:", recommendations)

# Evaluate recommendations
evaluation = evaluate_recommendations(recommendations)
st.write(f"Evaluation of recommendations: {evaluation}")

# Self-improvement module
adapt_recommendation_strategy(user_id, evaluation)
