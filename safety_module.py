ALLOWED_ITEMS = ['A', 'B', 'C', 'D']  # Safety boundary example

def filter_recommendations(recommended_items):
    return [item for item in recommended_items if item in ALLOWED_ITEMS]
