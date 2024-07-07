def find_primes(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = [i for i in range(1, num + 1) if num % i == 0]

    prime_factors = [factor for factor in set(factors) if is_prime(factor)]

    return prime_factors


print(find_primes(int(input("Enter a number: "))))