def rounded_avg(n, m):
    import math
    avg = (n + m) / 2
    return bin(int(math.ceil(avg)))[2:]