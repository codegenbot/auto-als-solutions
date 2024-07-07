def find_primes():
    num = int(input("Enter a number: "))
    factors = factorize(num)
    prime_factors = [
        factor for factor in factors if factor == 1 or math.isqrt(factor) ** 2 != factor
    ]
    return prime_factors


print(find_primes())