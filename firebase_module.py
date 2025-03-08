import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase():
    firebase_creds = {
        "type": st.secrets["firebase"]["type"],
        "project_id": st.secrets["firebase"]["project_id"],
        "private_key": st.secrets["firebase"]["private_key"].replace('\\n', '\n'),
        "client_email": st.secrets["firebase"]["client_email"],
        "token_uri": st.secrets["firebase"]["token_uri"],
    }
    cred = credentials.Certificate(firebase_creds)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            'databaseURL': st.secrets["firebase"]["database_url"]
        })

def get_user_feedback(user_id):
    ref = db.reference(f'feedback/{user_id}')
    return ref.get()

def save_user_feedback(user_id, feedback):
    ref = db.reference(f'feedback/{user_id}')
    ref.set(feedback)
