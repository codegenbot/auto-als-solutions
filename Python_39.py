def prime_fib(n: int):
    a = 0
    b = 1
    count = 1
    
    while True:
        if count == n:
            return b
        
        a, b = b, a + b
        
        if is_prime(b) and b > 2:
            count += 1

def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True