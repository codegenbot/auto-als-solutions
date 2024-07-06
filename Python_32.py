```
import math


def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero():
    xs = input("Enter coefficients separated by space: ").split()
    try:
        x = float(input("Enter the variable: "))
    except ValueError:
        print("Invalid input. Program terminated.")
        return

    if not xs or any(not str(i).lstrip('-').replace('.', '', 1).isnumeric() for i in xs):
        print("Invalid input. Program terminated.")
        return

    xs = [float(i) for i in xs]
    n = len(xs)
    if n % 2 == 1:
        raise ValueError("xs must have even number of coefficients")

    largest_coeff_index = n // 2
    result_x = -xs[largest_coeff_index] / xs[0]
    return round(result_x, 2)


print(find_zero())