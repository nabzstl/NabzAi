import streamlit as st
import pandas as pd
from recommendation_module import recommend_items
from firebase_module import initialize_firebase, get_user_feedback, save_user_feedback
from data_loader import load_data
from datetime import datetime

# Initialize Firebase
initialize_firebase()

# Load Data
user_item_matrix, similarity_df = load_data()

st.title("🤖 AI Recommendation Assistant")

# Chatbox for interaction
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def display_chat():
    for message, is_user in st.session_state.chat_history:
        if is_user:
            st.markdown(f"👤 **You:** {message}")
        else:
            st.markdown(f"🤖 **Assistant:** {message}")

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.setdefault('chat_history', []).append((True, user_input))
    
    user_id = user_input.strip()

    recommendations = recommend_items(user_input, user_item_matrix, similarity_df)
    
    response = "Here are recommendations based on your interests: " + ", ".join(recommendations)
    
    st.session_state['chat_history'].append((False, response))

    # save feedback to Firebase
    feedback = {
        "user_input": user_input,
        "recommendations": recommendations,
        "timestamp": datetime.utcnow().isoformat()
    }
    save_user_feedback(user_input, feedback)

# Display conversation
for is_user, message in st.session_state.get('chat_history', []):
    if is_user:
        st.markdown(f"👤 **You:** {message}")
    else:
        st.markdown(f"🤖 **Assistant:** {message}")
