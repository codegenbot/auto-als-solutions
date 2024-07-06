def find_zero(xs: list):
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
            coefficients = input("Enter coefficients (space separated): ")
            xs = [int(coeff) for coeff in coefficients.split()]
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