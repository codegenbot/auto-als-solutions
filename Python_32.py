import math


def find_zero(coeffs):
    a, b, c = coeffs
    discriminant = (b**2) - 4 * a * c
    if discriminant < 0:
        raise ValueError("Quadratic equation has no real roots")
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    return round(x1, 6)


def main():
    while True:
        try:
            num_coefficients = int(input("Enter number of coefficients: "))
            if num_coefficients % 2 != 0:
                print("Number of coefficients must be even. Try again.")
                continue
            coefficients = input("Enter coefficients (space separated): ")
            xs = [int(coeff) for coeff in coefficients.split()]
            break
        except ValueError as e:
            print(e)

    if len(xs) < 2:
        raise ValueError("xs must have at least two coefficients")
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")

    try:
        zero = find_zero([int(x), -1, 0])
        print(f"Zero of the quadratic equation is: {zero}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()