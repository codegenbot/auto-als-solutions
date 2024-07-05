```
result = None
while True:
    n = int(input("Enter the number of primes you want to see: "))
    if n > 0:
        result = prime_fib(n)
        break
print(result)
def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    a, b = 0, 1
    count = 0
    while True:
        if is_prime(b):
            if count == n - 1:
                return b
            count += 1
        a, b = b, a + b