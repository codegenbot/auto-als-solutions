import math

def rounded_avg(n, m):
    return bin((n + m) // 2)[2:].zfill(math.ceil(math.log2(((n + m) // 2) + 1)))