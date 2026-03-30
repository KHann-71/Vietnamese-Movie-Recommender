import numpy as np

def get_recall_at_k(actual, predicted, k=10):
    """Tính Recall@K: Tỷ lệ phim yêu thích nằm trong Top-K gợi ý"""
    act_set = set(actual)
    pred_set = set(predicted[:k])
    if len(act_set) == 0:
        return 0
    return len(act_set & pred_set) / float(len(act_set))

def get_ndcg_at_k(actual, predicted, k=10):
    """Tính nDCG@K: Chú trọng vị trí xếp hạng của phim phù hợp."""
    act_set = set(actual)
    dcg = 0.0
    for i, p in enumerate(predicted[:k]):
        if p in act_set:
            dcg += 1.0 / np.log2(i + 2)
    
    # Tính IDCG (Trường hợp lý tưởng nhất)
    idcg = 0.0
    for i in range(min(len(act_set), k)):
        idcg += 1.0 / np.log2(i + 2)
        
    return dcg / idcg if idcg > 0 else 0


