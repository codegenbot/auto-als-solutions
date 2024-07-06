```
def choose_num(x, y):
    if x > y:
        x, y = y, x
    for i in range(y, 0, -1):
        if (i-1) % 2 == 0 and (x+1) <= i:
            return i
    return -1