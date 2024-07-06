from typing import List


def find_primes(n: int) -> List[int]:
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for factor in range(2, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes