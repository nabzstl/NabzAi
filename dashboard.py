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

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("How can I assist you today?")
if prompt:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response (simple placeholder for now)
    with st.chat_message("assistant"):
        user_id = "user_demo"  # For demo purposes, ideally dynamic based on login/session
        recommendations = recommend_items(user_id, user_item_matrix, similarity_df)
        ai_response = f"I recommend the following items: **{', '.join(recommendations)}**"
        st.markdown(ai_response)

    # Save AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Optionally, save feedback to Firebase
    save_user_feedback(user_id, prompt)
