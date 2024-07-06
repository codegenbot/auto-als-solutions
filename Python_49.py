```
def modp(n: int, p: int):
    if n < 0:
        n += p
    return pow(n, p - 1, p)
# """
# This function calculates modular exponentiation. It adds the modulus to 
# negative numbers before performing the calculation.
# """