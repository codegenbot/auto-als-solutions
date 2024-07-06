def choose_num(x, y):
    if x % 2 == 0:
        return min(y, x + 2)
    else:
        for i in range(x, y+1):
            if i % 2 == 0:
                return i
        return -1