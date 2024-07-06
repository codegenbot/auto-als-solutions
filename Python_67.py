Here is the completed code:

def fruit_distribution(s,n):
    s = s.lower()
    x = int([i for i in map(str,filter(str.isdigit, s))][0])
    return n - x