import firebase_admin
from firebase_admin import credentials, db
import streamlit as st

def initialize_firebase():
    firebase_creds = {
        "type": "service_account",
        "project_id": "nabzai",
        "private_key_id": st.secrets["firebase"]["private_key_id"],
        "private_key": st.secrets["firebase"]["private_key"].replace('\\n', '\n'),
        "client_email": st.secrets["firebase"]["client_email"],
        "client_id": st.secrets["firebase"]["client_id"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
    }

    cred = credentials.Certificate(firebase_creds)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            'databaseURL': st.secrets["firebase"]["database_url"]
        })

def get_user_feedback(user_id):
    ref = db.reference(f"feedback/{user_id}")
    feedback = ref.get()
    return feedback if feedback else []

def save_user_feedback(user_id, feedback):
    ref = db.reference(f"feedback/{user_id}")
    ref.push(feedback)
