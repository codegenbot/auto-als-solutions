```
def fruit_distribution(s,n):
    s = s.replace('apples', 'apple')
    s = s.replace('oranges', 'orange')
    num_apple = int(s.split()[2].replace('apple', '')) if 'apple' in s else 0
    num_orange = int(s.split()[4].replace('orange', '')) if 'orange' in s else 0
    return n - num_apple - num_orange