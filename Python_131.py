```Python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= 1  # Set product to 1 when all are even
        else:
            product *= int(digit)
    return product