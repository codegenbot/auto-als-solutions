def find_zero(xs: list):
    if len(xs) < 2:
        raise ValueError("xs must have at least two coefficients")
    n = len(xs)
    if n % 2 != 0:
        raise ValueError("xs must have even number of coefficients")

    x = -sum(coeff for i, coeff in enumerate(xs) if i % 2 == 1) / sum(
        coeff for i, coeff in enumerate(xs) if i % 2 == 0
    )
    return round(x, 2)


def main():
    while True:
        try:
            num_coefficients = int(input("Enter number of coefficients: "))
            if num_coefficients < 2:
                raise ValueError("Number of coefficients must be at least 2")
            break
        except ValueError as e:
            print(e)

    while True:
        coefficients = input("Enter coefficients (space separated): ")
        try:
            xs = [int(coeff) for coeff in coefficients.split()]
            if len(xs) != num_coefficients:
                raise ValueError("Invalid number of coefficients")
            break
        except ValueError as e:
            print(e)

    try:
        result = find_zero(xs)
        if isinstance(result, int):
            print(f"The zero point is: {result}")
        else:
            print(f"The zero point is: {result:.2f}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()