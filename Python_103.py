def rounded_avg(n, m):
    if not isinstance(n, (int, float)) or not isinstance(m, (int, float)):
        return -1  

    avg = (n + m) / 2
    round_avg = round(avg)
    return bin(int(round_avg)).replace("0b", "")