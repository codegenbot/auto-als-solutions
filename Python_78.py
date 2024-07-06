def hex_key(num):
    primes = {'B': True, 'D': True}
    count = 0
    for digit in num:
        if digit.upper() in primes:
            count += 1
    return count