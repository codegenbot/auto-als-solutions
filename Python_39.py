def prime_fib(n: int):
    a, b = 2, 3
    if n == 1:
        return a
    if n == 2:
        return b
    for _ in range(2, n):
        a, b = b, 4 * b + a
        while not is_prime(b):
            b += 1
    return b


def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True