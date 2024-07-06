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
    while len(xs) % 2 != 0:
        if num_coefficients == len(xs):
            raise ValueError("xs must have even number of coefficients")
        new_coeff = input(f"Add more coefficients: ")
        xs += [int(coeff) for coeff in new_coeff.split()]

    if len(xs) < 3:
        print("Not enough coefficients to calculate any roots.")
    elif len(xs) % 2 == 1:
        raise ValueError("Number of coefficients must be even.")

    try:
        print(find_zero(xs))
    except ValueError as e:
        print(e)


def find_zero(coeffs):
    if len(coeffs) < 3:
        return "Not enough coefficients to calculate any roots."

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