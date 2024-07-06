```
def fruit_distribution(s,n):
    s = s.replace('apples and', 'apple and').replace('oranges and', 'orange and')
    s = s.replace(' apples ', ' apple ').replace(' oranges ', ' orange ')
    s = s.replace('apples', '0').replace('oranges', '0')
    return n - int(s.split()[2].replace('apple', '0').replace('orange', '0'))