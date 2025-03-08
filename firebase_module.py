import firebase_admin
from firebase_admin import credentials, db
import streamlit as st

def initialize_firebase():
    firebase_creds = {
        "type": st.secrets["firebase"]["type"],
        "project_id": st.secrets["firebase"]["project_id"],
        "private_key_id": st.secrets["firebase"]["private_key_id"],
        "private_key": st.secrets["firebase"]["private_key"].replace('\\n', '\n'),
        "client_email": st.secrets["firebase"]["client_email"],
        "client_id": st.secrets["firebase"]["client_id"],
        "auth_uri": st.secrets["firebase"].get("auth_uri", "https://accounts.google.com/o/oauth2/auth"),
        "token_uri": st.secrets["firebase"].get("token_uri", "https://oauth2.googleapis.com/token"),
        "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"],
        "universe_domain": st.secrets["firebase"].get("universe_domain", "googleapis.com")
    }

    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://nabzai-default-rtdb.firebaseio.com'
    })
