```
def find_zero():
    while True:
        try:
            coeffs = [int(x) for x in input("Enter coefficients separated by spaces: ").split()]
            if len(coeffs) < 2:
                raise ValueError("xs must have at least two coefficients")
            n = len(coeffs)
            if n % 2 != 0:
                raise ValueError("xs must have even number of coefficients")
            x = -sum(coeff for i, coeff in enumerate(coeffs) if i % 2 == 1) / sum(
                coeff for i, coeff in enumerate(coeffs) if i % 2 == 0
            )
            return round(x, 2)
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Try again.")