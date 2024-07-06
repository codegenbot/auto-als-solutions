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
    a, b, c = coeffs[:3]
    d = coeffs[3:]
    roots = []
    for i in range(0, len(d), 2):
        temp = [a, 2 * a * d[i], c - (d[i + 1]) ** 2]
        root = (-temp[1] + math.sqrt((temp[1]) ** 2 - 4 * temp[0] * temp[2])) / (
            2 * temp[0]
        )
        roots.append(-d[i] / root)
    return roots


if __name__ == "__main__":
    main()