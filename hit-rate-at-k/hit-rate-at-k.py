import numpy as np

def hit_rate_at_k(all_recommended, all_relevant, k):
    """
    Compute Hit Rate@K over multiple users.

    Parameters:
        all_recommended : list of lists
            Recommended items for each user.
        all_relevant : list of lists
            Relevant items for each user.
        k : int

    Returns:
        float
            Hit Rate@K
    """

    hits = 0
    num_users = len(all_recommended)

    for recommended, relevant in zip(all_recommended, all_relevant):
        recommended_k = recommended[:k]
        relevant = set(relevant)

        if len(set(recommended_k) & relevant) > 0:
            hits += 1

    return hits / num_users if num_users > 0 else 0.0