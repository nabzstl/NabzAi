import streamlit as st
import pandas as pd
from recommendation_module import recommend_items
from firebase_module import initialize_firebase, get_user_feedback, save_user_feedback
from data_loader import load_data

# Initialize Firebase
initialize_firebase()

# Load Data
user_item_matrix, similarity_df = load_data()

st.title("🤖 AI Recommendation Assistant")

# Get user input
user_input = st.text_input("Say something...")

if user_input:
    user_id = 'test_user'
    
    # Provide recommendations based on user input
    recommendations = recommend_items(user_id, user_item_matrix, similarity_df)
    st.write(f"I recommend the following items: {', '.join(recommendations)}")

    # Optional: Save feedback
    feedback = {"input": user_input, "recommendations": recommendations}
    save_user_feedback(user_id, feedback)

# Display feedback (optional, for debugging or transparency)
feedback_data = get_user_feedback(user_id='test_user')

if feedback_data:
    st.subheader("User Feedback")
    feedback_df = pd.DataFrame.from_dict(feedback_data, orient='index')
    st.write(feedback_df)

st.success("App loaded successfully!")
