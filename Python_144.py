```
def simplify(x, n):
    x_numer, x_denom = map(int, x.split('/'))
    n_numer, n_denom = map(int, n.split('/'))

    product_numer = x_numer * n_numer
    product_denom = x_denom * n_denom

    return product_numer == product_denom