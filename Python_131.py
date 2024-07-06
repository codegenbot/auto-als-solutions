def digits(n):
    max_digit = 0
    for digit in str(n):
        if int(digit) % 2 != 0 and int(digit) > max_digit:
            max_digit = int(digit)
    return max_digit or 0