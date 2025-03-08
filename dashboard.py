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

user_input = st.text_input("Enter your user ID:")

if user_input:
    try:
        recommendations = recommend_items(
            user_id=user_input,
            user_item_matrix=user_item_matrix,
            similarity_df=similarity_df
        )
        st.write(f"Recommendations for {user_input}: {', '.join(recommendations)}")
    except KeyError:
        st.warning("User ID not found. Showing popular recommendations instead.")
        popular_recommendations = user_item_matrix.sum().sort_values(ascending=False).head(5).index.tolist()
        st.write(f"Popular recommendations: {', '.join(popular_recommendations)}")

# Feedback section
with st.form("feedback_form"):
    feedback_text = st.text_area("Provide feedback or suggest new items:")
    submit_feedback = st.form_submit_button("Submit Feedback")
    if submit_feedback and user_input:
        save_user_feedback(user_input, {"feedback": feedback_df})
        st.success("Thanks for your feedback!")

# Display feedback (optional, for debugging or transparency)
feedback_df = get_user_feedback(user_id='test_user')
if feedback_df is not None and not feedback_df.empty:
    st.subheader("User Feedback")
    st.write(feedback_df)
