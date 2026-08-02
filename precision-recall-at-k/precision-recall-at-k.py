import numpy as np
def precision_recall_at_k(recommended, relevent, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    recom_k=recommended[:k]
    relevent=set(relevent)
    union=len(set(recom_k) & relevent)

    precision=union/k if k>0 else 0
    recall=union/len(relevent)if len(relevent)>0 else 0

    return [precision,recall]
    # Write code here