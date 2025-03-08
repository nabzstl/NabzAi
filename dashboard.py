import streamlit as st
import pandas as pd
from recommendation_module import recommend_items
from firebase_module import initialize_firebase, get_user_feedback, save_user_feedback
from data_loader import load_data

# Initialize Firebase at startup
initialize_firebase()

# Load data (cached)
user_item_matrix, similarity_df = load_data()

st.title("🤖 AI Recommendation Assistant")

# User input
user_input = st.text_input("Enter your User ID:")

if user_input := user_input.strip():
    try:
        # Get recommendations
        recommendations = recommend_items(
            user_id=user_input,
            user_item_matrix=user_item_matrix,
            similarity_df=similarity_df
        )
        
        st.write(f"I recommend the following items: {', '.join(recommendations)}")

        # Save feedback (optional)
        feedback = {"recommendations": recommendations}
        save_user_feedback(user_id=user_input, feedback_data=feedback)

        # Retrieve and display previous user feedback (optional)
        feedback_data = get_user_feedback(user_input)
        if feedback_data:
            feedback_df = pd.DataFrame([feedback_data])
            st.subheader("User Feedback")
            st.write(feedback_df)

    except KeyError:
        st.error("User ID not found. Please enter a valid User ID.")
