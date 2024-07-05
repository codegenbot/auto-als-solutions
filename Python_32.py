```
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
    num_coefficients = int(input("Enter number of coefficients: "))
    xs = [int(i) for i in input("Enter coefficients (space separated): ").split()]

    if num_coefficients != len(xs):
        print("Invalid number of coefficients entered.")
        exit()

    try:
        print(find_zero(xs))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()