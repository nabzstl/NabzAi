import joblib
import os

MODEL_PATH = 'user_similarity.pkl'

def save_model(model):
    joblib.dump(model, MODEL_PATH)

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def retrain_model(user_item_matrix, similarity_function):
    similarity_df = similarity_function(user_item_matrix)
    save_model(similarity_df)
    return similarity_df
