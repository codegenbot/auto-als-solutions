def factorize(num):
    if num < 2:
        return [1]
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return [i] + factorize(num // i)
    return [num]

def find_primes():
    num = int(input("Enter a number: "))
    factors = factorize(num)
    prime_factors = [factor for factor in set(factors) if all(factor % n != 0 for n in range(2, int(math.isqrt(factor)) + 1))]
    return prime_factors

print(find_primes())