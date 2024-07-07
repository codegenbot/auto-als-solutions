```
def find_primes():
    num = int(input("Enter a number: "))
    factors = [i for i in range(1, num + 1) if num % i == 0]
    prime_factors = [
        factor for factor in set(factors) if all(num % i > 0 for j in range(2, int(i ** 0.5) + 1))
    ]
    return prime_factors


print(find_primes())