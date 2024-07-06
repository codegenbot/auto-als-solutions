def hex_key(num):
    primes = {"B": True, "D": True, "F": False}
    count = sum(1 for c in num if c.upper() in primes)
    return count