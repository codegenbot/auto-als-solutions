def find_primes():
    num = int(input("Enter a number: "))
    factors = factorize(num)
    prime_factors = [
        factor for factor in set(factors) if all(math.isqrt(factor) ** 2 != factor and i * factor != num for i in range(1, math.isqrt(factor)) + [factor])
    ]
    return prime_factors

print(find_primes())