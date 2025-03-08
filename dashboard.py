import streamlit as st
import pandas as pd
from data_module import load_data
from recommendation_module import compute_user_similarity, recommend_items
from evaluation_module import evaluate_recommendations
from self_improvement_module import adapt_recommendation_strategy
import firebase_module

# Initialize Firebase
firebase_module.initialize_firebase()

# Title of your Dashboard
st.title('AI Recommendation System Dashboard')

# Load data
user_item_matrix = load_data()
similarity_df = compute_user_similarity(user_item_matrix)

# Sidebar for user inputs
st.sidebar.header('Control Panel')
user_id = st.sidebar.selectbox('Select User ID', user_item_matrix.index)
initial_top_n = st.sidebar.slider('Initial Number of Recommendations', 1, 5, 2)

# Sidebar for user feedback
st.sidebar.header('User Feedback Simulation')
feedback_item_1 = st.sidebar.selectbox('Feedback Item 1', user_item_matrix.columns)
feedback_rating_1 = st.sidebar.slider('Rating Item 1', 1, 5, 4)

feedback_item_2 = st.sidebar.selectbox('Feedback Item 2', user_item_matrix.columns, index=1)
feedback_rating_2 = st.sidebar.slider('Rating Item 2', 1, 5, 5)

user_feedback = {feedback_item_1: feedback_rating_1, feedback_item_2: feedback_rating_2}

# Save feedback to Firebase
if st.sidebar.button('Submit Feedback'):
    firebase_module.save_user_feedback(user_id, user_feedback)
    st.sidebar.success('Feedback successfully saved to Firebase!')

# Retrieve feedback history from Firebase
feedback_history = firebase_module.get_user_feedback(user_id)

if feedback_history is None:
    feedback_history = [user_feedback]
else:
    feedback_history = list(feedback_history.values())

# Run recommendations
top_n = initial_top_n

st.subheader('Recommendation & Adaptation Cycles')
for cycle, feedback in enumerate(feedback_history, 1):
    recommended = recommend_items(user_id, user_item_matrix, similarity_df, top_n)
    evaluation_score = evaluate_recommendations(recommended, feedback)

    st.write(f'**Cycle {cycle}:** Recommended items: `{recommended}` | Evaluation Score: `{evaluation_score}`')

    top_n = adapt_recommendation_strategy(evaluation_score, top_n)
    st.write(f'Adapted number of recommendations for next cycle: `{top_n}`')
    st.write('---')