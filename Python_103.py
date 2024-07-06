def rounded_avg(a, b):
    import math
    avg = math.ceil((a + b) / 2)
    return bin(int(str(avg), 2))[2:]