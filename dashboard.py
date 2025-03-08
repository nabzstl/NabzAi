import streamlit as st
from recommendation_module import compute_user_similarity, recommend_items
from evaluation_module import evaluate_recommendations
from self_improvement_module import adapt_recommendation_strategy
import firebase_module

firebase_module.initialize_firebase()

# Dashboard Title
st.title('AI Recommendation System Dashboard')

# User ID
user_id = st.text_input('Enter User ID:')

if user_id := st.session_state.get('user_id'):
    st.write(f"Logged in as: {user_id}")

# Input for user to provide feedback or queries
user_query = st.text_area("Enter your query or feedback:")

if st.button("Submit"):
    if user_query:
        firebase_module.save_user_feedback(user_id, user_query)
        st.success('Feedback successfully saved!')

# Retrieve feedback history from Firebase
feedback_history = firebase_module.get_user_feedback(user_id)

# Display previous feedback or chat history
st.subheader("Chat and Feedback History")
if feedback_history:
    for idx, feedback in enumerate(feedback_history, 1):
        st.chat_message("user").write(feedback)

# Generate recommendations based on feedback
recommendations = recommend_items(user_id, user_item_matrix, similarity_df)
st.write("Recommended items:", recommendations)

evaluation = evaluate_recommendations(recommendations)
st.write("Evaluation results:", evaluation)

adapted_strategy = adapt_recommendation_strategy(evaluation)
st.write("Strategy adapted to:", adapted_strategy)
