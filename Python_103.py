def rounded_avg(n, m):
    import math
    avg = math.ceil((n + m) / 2)
    return bin(int(avg))[2:].zfill(len(bin(int(avg)))[2:])