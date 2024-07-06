```
import math

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
        print(find_zero(xs))
    except ValueError as e:
        print(e)


def find_zero(coeffs):
    a, b, c = coeffs
    discriminant = (b**2) - 4*a*c
    if discriminant < 0:
        raise ValueError("Quadratic equation has no real roots")
    return (-b + math.sqrt(discriminant)) / (2 * a)


if __name__ == "__main__":
    main()