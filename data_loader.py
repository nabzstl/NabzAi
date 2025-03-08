# data_loader.py
import pandas as pd

@st.cache_data
def load_data():
    user_item_matrix = pd.read_csv('user_item_matrix.csv')
    similarity_df = pd.read_csv('similarity_df.csv')
    return user_item_matrix, similarity_df
