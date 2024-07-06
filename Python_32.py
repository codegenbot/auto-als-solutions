import math


def main():
    while True:
        try:
            num_coefficients = int(input("Enter number of coefficients: "))
            if num_coefficients % 2 != 0:
                print("Number of coefficients must be even. Try again.")
                continue
            break
        except ValueError as e:
            print(e)

    xs = [
        int(coeff)
        for coeff in (input("Enter coefficients (space separated): ") + " ").split()
    ]

    if len(xs) != num_coefficients:
        raise ValueError("Invalid number of coefficients. Try again.")

    try:
        print(find_zero(xs))
    except ValueError as e:
        print(e)


def find_zero(coeffs):
    a, b, c = coeffs[:3]
    d = coeffs[3:]
    if len(d) % 2 != 0:
        raise ValueError("Invalid number of coefficients. Try again.")
    roots = []
    for i in range(0, len(d), 2):
        temp = [a, 2 * a * d[i], c - (d[i + 1]) ** 2]
        try:
            root = (-temp[1] + math.sqrt((temp[1]) ** 2 - 4 * temp[0] * temp[2])) / (
                2 * temp[0]
            )
            roots.append(-d[i] / root)
        except (ZeroDivisionError, ValueError) as e:
            print(f"Failed to calculate a root: {e}")
    return roots


if __name__ == "__main__":
    main()