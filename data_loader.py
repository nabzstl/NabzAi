import pandas as pd
import streamlit as st
from recommendation_module import compute_user_similarity

@st.cache_data
def load_data():
    user_item_matrix = pd.read_csv('user_item_matrix.csv')
    similarity_df = compute_user_similarity(user_item_matrix)
    return user_item_matrix, similarity_df
