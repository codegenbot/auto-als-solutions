```
def hex_key(num):
    primes = set([2, 3, 5, 7, 11, 13, 17])
    prime_count = 0
    for digit in num.upper():
        if digit.isdigit():
            if int(digit) in primes:
                prime_count += 1
        elif 'A' <= digit <= 'F':
            if (int(digit, 16) + 1) % 3 == 0 or (int(digit, 16) - 4) % 12 == 0 or int(digit, 16) % 20 == 9:
                prime_count += 1
    return prime_count