def main():
    num_coefficients = int(input("Enter number of coefficients: "))
    xs_input = input(f"Enter {num_coefficients} coefficients (space separated): ")

    try:
        xs = [int(i) for i in xs_input.split()]

        print(find_zero(xs))
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Invalid input. Please enter valid integers.")


def find_zero(xs):
    if len(xs) < 2:
        raise ValueError("xs must have at least two coefficients")
    n = len(xs)
    if n % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    x = -sum(coeff for i, coeff in enumerate(xs) if i % 2 == 1) / sum(
        coeff for i, coeff in enumerate(xs) if i % 2 == 0
    )
    return round(x, 2)


if __name__ == "__main__":
    main()