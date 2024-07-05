```
def find_zero():
    while True:
        try:
            xs = [int(i) for i in input("Enter coefficients separated by space: ").split()]
            if len(xs) < 2:
                raise ValueError("xs must have at least two coefficients")
            n = len(xs)
            if n % 2 != 0:
                raise ValueError("xs must have even number of coefficients")
            x = -sum(coeff for i, coeff in enumerate(xs) if i % 2 == 1) / sum(
                coeff for i, coeff in enumerate(xs) if i % 2 == 0
            )
            return round(x, 2)
        except ValueError as e:
            print(f"Error: {str(e)}")