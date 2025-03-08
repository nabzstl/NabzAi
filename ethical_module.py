UNETHICAL_ITEMS = ['D']  # Example of items deemed unethical/inappropriate

def enforce_ethics(recommended_items):
    return [item for item in recommended_items if item not in UNETHICAL_ITEMS]
