def count_upper(s):
    if not s:  
        return 0
    return sum(1 for i, c in enumerate(s) if i % 2 == 0 and c.upper() in 'AEIOU')