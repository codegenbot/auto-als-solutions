def choose_num(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return min(y, max(x, 2))
    else:
        for i in range(max(x, 2), min(y+1, y)):
            if i % 2 == 0:
                return i
        return -1