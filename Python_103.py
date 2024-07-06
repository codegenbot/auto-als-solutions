```
def rounded_avg(n, m):
    import math
    avg = (n + m) / 2
    return format(int(math.ceil(avg)), 'b')[2:]