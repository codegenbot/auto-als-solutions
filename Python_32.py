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
        roots = find_zero(xs)
        for root in roots:
            print(root)
    except Exception as e:
        print(f"Program did not receive expected input: {e}")


def find_zero(coeffs):
    a, b, c = coeffs[:3]
    d = coeffs[3:]
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