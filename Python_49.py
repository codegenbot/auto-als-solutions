def modp(n: int, p: int) -> int:
    def egcd(a: int, b: int) -> tuple[int, int, int]:
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, y, x = egcd(b, a % b)
            return (gcd, y - (a // b) * x, x)

    g, y, x = egcd(n, p)
    if g != 1:
        return None
    else:
        return pow(x, p - 2, p)