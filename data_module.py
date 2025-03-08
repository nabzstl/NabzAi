import pandas as pd

def load_data():
    data = {
        'user_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        'item_id': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'D', 'C', 'D'],
        'rating': [5, 3, 4, 2, 2, 5, 4, 3, 5, 4]
    }
    df = pd.DataFrame(data)
    user_item_matrix = df.pivot_table(index='user_id', columns='item_id', values='rating').fillna(0)
    return user_item_matrix
