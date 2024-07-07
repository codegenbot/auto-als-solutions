```
def find_primes():
    num = int(input("Enter a number: "))
    prime_factors = [i for i in range(2, num + 1) if num % i == 0 and all(num % j > 0 for j in range(2, int(i ** 0.5) + 1))]
    return list(set(prime_factors))