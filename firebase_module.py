import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st

def initialize_firebase():
    firebase_creds = {
        # credentials here
    }
    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred, {
        'databaseURL': st.secrets["firebase"]["database_url"]
    })

def get_user_feedback(user_id):
    db = firestore.client()
    feedback_ref = db.collection('feedback').document(user_id)
    feedback = feedback_ref.get()
    if feedback.exists:
        return feedback.to_dict()
    else:
        return {}

def save_user_feedback(user_id, feedback):
    db = firestore.client()
    feedback_ref = db.collection('feedback').document(user_id)
    feedback_ref.set(feedback)
