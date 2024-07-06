```Python
def rounded_avg(n, m):
    return bin((n + m) // 2)[2:].zfill(math.floor(math.log2((n + m) // 2)) + 1)