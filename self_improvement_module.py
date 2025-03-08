def adapt_recommendation_strategy(evaluation_score, current_top_n):
    # Basic logic: if performance is low, recommend more items; if high, fewer items
    if evaluation_score < 3:
        return min(current_top_n + 1, 5)
    elif evaluation_score > 4:
        return max(current_top_n - 1, 1)
    else:
        return current_top_n
