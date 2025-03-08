import streamlit as st
from recommendation_module import compute_user_similarity, recommend_items
from evaluation_module import evaluate_recommendations
from self_improvement_module import adapt_recommendation_strategy
import firebase_module
from firebase_module import get_user_feedback, save_user_feedback
from data_loader import load_data

# Initialize Firebase
firebase_module.initialize_firebase()

# Title
st.title('AI Recommendation System Dashboard')

# Load or compute user-item matrix and similarity dataframe
@st.cache_data
def load_similarity_data():
    user_item_matrix, similarity_df = compute_user_similarity()
    return user_item_matrix, similarity_df

user_item_matrix, similarity_df = load_similarity_data()

# User ID input
user_id = st.text_input('Enter User ID:', 'user123')

# Chat interface for user feedback
with st.container():
    st.write("### Chat with the Recommendation AI")
    feedback = st.chat_input("Provide your feedback or ask for recommendations")

    if feedback:
        with st.chat_message("user"):
            st.write(feedback)
        
        # Save user feedback to Firebase
        from firebase_module import save_user_feedback
        save_user_feedback(user_id, feedback)
        st.sidebar.success('Feedback successfully saved to Firebase!')

# Retrieve feedback history
from firebase_module import get_user_feedback
feedback_history = get_user_feedback(user_id)

# Display chat history
if feedback_history:
    for fb in feedback_history:
        with st.chat_message("user"):
            st.write(f"{fb}")

# Generate and display recommendations
recommendations = recommend_items(user_id, user_item_matrix, similarity_df)

with st.chat_message("assistant"):
    st.write("Here are your recommended items:")
    for item in recommendations:
        st.write(f"- {item}")

# Evaluate recommendations
evaluation = evaluate_recommendations(recommendations)
st.sidebar.write("Recommendation Evaluation:", evaluation)

# Self-improvement based on user feedback and evaluations
adapted_strategy = adapt_recommendation_strategy(user_id, feedback, recommendations)
st.sidebar.info(f"Adapted Recommendation Strategy: {adapt_recommendation_strategy}")
