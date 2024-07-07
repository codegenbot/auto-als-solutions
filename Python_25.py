def find_primes():
    num = int(input("Enter a number: "))
    div = int(input("Enter a divisor: "))
    factors = [i for i in range(1, num + 1) if num % i == 0]
    prime_factors = [
        factor for factor in set(factors) if all(num % i > 0 for j in range(2, int(factor ** 0.5) + 1))
    ]
    return [factor for factor in prime_factors if factor <= div]

print(find_primes())