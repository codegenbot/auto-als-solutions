```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_factors = []
    for i in range(2, a // 2 + 1):
        while a % i == 0:
            if is_prime(i):
                prime_factors.append(i)
            a //= i
    if len(prime_factors) >= 3:
        return all(is_prime(f) for f in prime_factors)
    else:
        return False