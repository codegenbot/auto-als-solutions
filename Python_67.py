def fruit_distribution(s,n):
    s = s.lower()
    start = s.find('and') + 4
    apples = int(s[:start-1].split()[-1][:-7])
    n -= apples
    return n