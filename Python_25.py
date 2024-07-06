from typing import List
import math


def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            if i > math.sqrt(n):
                break
            n //= i
            if i not in factors:
                factors.append(i)
    return factors