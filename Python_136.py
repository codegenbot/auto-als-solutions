```
def largest_smallest_integers(lst):
    neg = [x for x in lst if x < 0]
    pos = [x for x in lst if x > 0]
    
    if len(neg) == 0:
        return None, min(pos) if pos else None
    elif len(pos) == 0:
        return max(neg), None
    else:
        return max(neg), min(pos)