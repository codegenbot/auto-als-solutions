```
def digits(n):
    has_odd = False
    product = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            has_odd = True
            product *= int(digit)
    return product if has_odd else 0