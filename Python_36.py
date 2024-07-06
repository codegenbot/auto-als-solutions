def fizz_buzz(n: int):
    count = 0
    for i in range(max(14, n-1), 12, -13):
        str_i = str(i)
        if '7' in str_i:
            count += 1
    return count