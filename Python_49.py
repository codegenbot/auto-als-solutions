def modp(n: int, p: int):
    """Calculate n^p-1 (mod p)"""
    if n < 0:
        n += p
    return pow(n, p - 1, p)