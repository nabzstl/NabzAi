import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

def initialize_firebase():
    firebase_creds = {
        "type": st.secrets["firebase"]["type"],
        "project_id": st.secrets["firebase"]["project_id"],
        "private_key_id": st.secrets["firebase"]["private_key_id"],
        "private_key": st.secrets["firebase"]["private_key"].replace('\\n', '\n'),
        "client_email": st.secrets["firebase"]["client_email"],
        "client_id": st.secrets["firebase"]["client_id"],
        "auth_uri": st.secrets["firebase"]["auth_uri"],
        "token_uri": st.secrets["firebase"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"],
        "universe_domain": st.secrets["firebase"]["universe_domain"]
    }

    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred, {
        'databaseURL': st.secrets["firebase"]["database_url"]
    })

def save_user_feedback(user_id, feedback):
    ref = db.reference(f'feedback/{user_id}')
    ref.push(feedback)

def get_user_feedback(user_id):
    ref = db.reference(f'feedback/{user_id}')
    return ref.get()
