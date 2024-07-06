def find_zero(xs: list):
    n = len(xs)
    if n < 2:
        raise ValueError("xs must have at least two coefficients")
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
                print("Number of coefficients must be at least 2. Try again.")
                continue
            if num_coefficients % 2 != 0:
                print("Number of coefficients must be even. Try again.")
                continue

            coefficients = input(f"Enter {num_coefficients} coefficients (space separated): ")
            xs = [int(coeff) for coeff in coefficients.split()]
            break
        except ValueError as e:
            print(e)

    try:
        print(find_zero(xs))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()