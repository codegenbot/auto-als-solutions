def rounded_avg(n, m):
    if n == m == 0:
        return str(0)
    avg = (n + m) / 2
    if avg.is_integer():
        return bin(int(avg))[2:]
    else:
        return "Error: Average is not an integer."