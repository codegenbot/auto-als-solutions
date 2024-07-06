def rounded_avg(n, m):
    import math
    avg = math.ceil((n + m) / 2)
    return bin(avg)[2:].zfill(math.floor(math.log2(avg)) + 1)