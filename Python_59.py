```
def largest_prime_factor(n: int):
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True

    largest = 1
    for possible_prime in range(2, n + 1):
        if is_prime(possible_prime) and n % possible_prime == 0:
            largest = max(largest, possible_prime)
    return largest