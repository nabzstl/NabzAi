import pandas as pd
import streamlit as st
from recommendation_module import compute_user_similarity

@st.cache_data
def load_data():
    user_item_matrix = pd.read_csv("user_item_matrix.csv", index_col=0)

    # Ensuring numeric type (force numeric and fill errors with zeros)
    user_item_matrix = user_item_matrix.apply(pd.to_numeric, errors='coerce').fillna(0)

    similarity_df = compute_user_similarity(user_item_matrix)

    return user_item_matrix, similarity_df
