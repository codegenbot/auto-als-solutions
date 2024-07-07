```
def find_primes():
    num = int(input("Enter a number: "))
    prime_factors = [i for i in range(2, num + 1) if num % i == 0 and is_prime(i)]
    return prime_factors

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(find_primes())