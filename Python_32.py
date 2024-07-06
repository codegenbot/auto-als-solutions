Here is the solution to the problem:

def find_zero(xs: list):
    n = len(xs)
    assert n % 2 == 0, "Input coefficients must have even number of elements"
    max_coeff = abs(max(xs))
    return -xs[1] / xs[0]

Note that the above code assumes that the largest coefficient in the polynomial is not zero, as stated in the problem description.