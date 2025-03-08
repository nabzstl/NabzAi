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

# User input
user_input = st.text_input("Enter your user ID:")

if user_input := user_input.strip():
    try:
        # Fetch recommendations based on provided user_id
        recommendations = recommend_items(
            user_id=user_input,
            user_item_matrix=user_item_matrix,
            similarity_df=similarity_df
        )

        st.write(f"I recommend the following items: {', '.join(recommendations)}")

        # Save feedback to Firebase
        feedback = {
            "recommended_items": recommendations
        }
        save_user_feedback(user_input, feedback_data=feedback)

        # Displaying user feedback
        feedback_data = get_user_feedback(user_input)
        if feedback_data:
            feedback_df = pd.DataFrame([feedback_data])
            st.subheader("User Feedback")
            st.write(feedback_df)
            
if user_input:
    try:
        recommendations = recommend_items(
            user_id=user_input,
            user_item_matrix=user_item_matrix,
            similarity_df=similarity_df
        )
        st.write(f"I recommend the following items: {', '.join(recommendations)}")
        
        # Save feedback to Firebase
        feedback = {"recommended_items": recommendations}
        save_user_feedback(user_input, feedback)

    except KeyError:
        st.warning("Your user ID was not found, showing general recommendations.")
        recommendations = user_item_matrix.sum().sort_values(ascending=False).head(5).index.tolist()
        st.write(f"Popular recommendations: {', '.join(recommendations)}")


    except KeyError:
        st.error("User ID not found. Please enter a valid User ID.")
