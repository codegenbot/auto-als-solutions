```
def fruit_distribution(s,n):
    s = s.replace('apples and ', '')
    s = s.replace(' oranges', '')
    total_fruits = int(s) + n - (int(s.split(' ')[0]) + int(s.split(' ')[4]))
    return total_fruits