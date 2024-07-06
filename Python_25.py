```
import math
from typing import List


def factorize():
    while True:
        try:
            n = int(input("Enter a number to factorize: "))
            if n < 1:
                print("Please enter a positive integer.")
            else:
                factors = []
                i = 2
                while i * i <= n:
                    if n % i:
                        i += 1
                    else:
                        n //= i
                        count = 0
                        while n % i == 0:
                            n //= i
                            count += 1
                        factors.append([i] * count)
                if n > 1:
                    factors.append([n])
                return [factor for factor in factors]
        except ValueError:
            print("Invalid input. Please enter an integer.")


print(factorize())