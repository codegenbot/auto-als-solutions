```
def rounded_avg(n, m):
    from math import ceil
    avg = (n + m) / 2
    return bin(int(ceil(avg)))[2:]