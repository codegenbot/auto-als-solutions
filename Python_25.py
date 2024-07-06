```Python
from typing import List
import math


def factorize(n: int) -> List[int]:
    if n <= 0:
        raise ValueError("n should be greater than zero")
    elif n < 2:
        return [n]
    else:
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                count = 0
                while n % (i * i) == 0:
                    count += 1
                    n //= i * i
                for _ in range(count):
                    factors.append(i)
                n = max(2, int(math.sqrt(n)))
        if n > 1:
            factors.append(n)
        return factors