```
def largest_prime_factor(n: int):
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True

    i = n // 2
    while i > 1:
        if n % i == 0:
            if is_prime(i):
                j = i
                while j <= i and n % j == 0:
                    j += 1
                return i if j == i else j
        i -= 1