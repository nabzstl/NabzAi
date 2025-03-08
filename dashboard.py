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

# Prompt the user to enter their user ID
user_id = st.text_input("Enter your User ID:")

if user_id:
    user_id = user_id.strip()
    # Generate recommendations
    try:
        recommendations = recommend_items(user_id, user_item_matrix, similarity_df)
        st.write(f"I recommend the following items: {', '.join(recommendations)}")

        # Optional: Save feedback
        feedback = {
            "recommendations": recommendations
        }
        save_user_feedback(user_id, feedback)

    except KeyError:
        st.error(f"User ID '{user_id}' not found. Please try another user ID.")

    # Display feedback (optional, for debugging or transparency)
    feedback_data = get_user_feedback(user_id=user_id)
    if feedback_data:
        feedback_df = pd.DataFrame([feedback_data])
        st.subheader("User Feedback")
        st.write(feedback_df)
else:
    st.info("Please enter your User ID to receive recommendations.")

# Initialize Firebase once at start-up
initialize_firebase()
