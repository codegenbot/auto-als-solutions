```
def simplify(x, n):
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    common_divisor = max(x_num, x_denom)
    while common_divisor > 1 and x_num % common_divisor == 0 and x_denom % common_divisor == 0:
        x_num //= common_divisor
        x_denom //= common_divisor

    common_divisor = max(n_num, n_denom)
    while common_divisor > 1 and n_num % common_divisor == 0 and n_denom % common_divisor == 0:
        n_num //= common_divisor
        n_denom //= common_divisor

    if x_num * n_denom == x_denom * n_num:
        return True
    else:
        return False