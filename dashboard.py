import streamlit as st
import pandas as pd
from recommendation_module import recommend_items
from firebase_module import initialize_firebase, get_user_feedback, save_user_feedback
from data_loader import load_data

# Initialize Firebase
initialize_firebase()

# Load data (cached for efficiency)
user_item_matrix, similarity_df = load_data()

st.title("🤖 AI Recommendation Assistant")

# User input
user_input = st.text_input("Say something to get recommendations:")

if user_input:
    recommendations = recommend_items(user_input, user_item_matrix, similarity_df)

    if recommendations == ["No recommendations found (user not in database)."]:
        st.write(recommendations[0])
    else:
        st.write(f"I recommend the following items: {', '.join(recommendations)}")

# User feedback collection
with st.expander("Provide Feedback"):
    feedback_text = st.text_area("Your feedback:")
    if st.button("Submit Feedback"):
        save_user_feedback(user_input, feedback=feedback_text)
        st.success("Thanks for your feedback!")

# Display feedback (optional, for debugging or transparency)
feedback_df = get_user_feedback()
if not feedback_df.empty:
    st.subheader("User Feedback")
    st.write(feedback_df)