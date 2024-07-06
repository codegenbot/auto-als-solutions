def modp(n: int, p: int):
    if n < 0:
        n += p
    return pow((n * (1 << ((p - 2).bit_length() + 1))) % p, p - 1, p)