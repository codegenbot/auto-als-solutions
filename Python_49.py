def modp(m, p):
    n = m % p
    if n < 0:
        n += p
    return n