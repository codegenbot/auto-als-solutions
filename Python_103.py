def average_rounding_score(scores):
    return sum(map(round, scores)) / len(scores) if scores else -1