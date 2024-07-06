```
def fruit_distribution(s,n):
    s = s.split()
    apples = int(''.join(filter(str.isdigit, [x for x in s if 'apples' in x])))/2
    oranges = int(''.join(filter(str.isdigit, [x for x in s if 'oranges' in x])))/2
    return n - apples - oranges