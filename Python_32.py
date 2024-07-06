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
        print("Not enough coefficients to find a root.")
        return

    try:
        print(find_zero(xs))
    except ValueError as e:
        print(e)


def find_zero(coeffs):
    roots = []
    i = 0
    while i < len(coeffs) - 1:
        if i + 2 > len(coeffs) - 1:
            break
        a, b, c = coeffs[i], coeffs[i + 1], coeffs[i + 2]
        d = coeffs[i + 3 :]
        if not d:
            temp = [a, 2 * a * b, c]
            try:
                root = (-temp[1] + math.sqrt((temp[1]) ** 2 - 4 * temp[0] * c)) / (
                    2 * temp[0]
                )
                roots.append(-b / root)
            except (ZeroDivisionError, ValueError) as e:
                print(f"Failed to calculate a root: {e}")
        else:
            while len(d) % 2 != 0:
                new_coeff = input(f"Add more coefficients for degree {len(d)+3}: ")
                d += [int(coeff) for coeff in new_coeff.split()]
            for j in range(0, len(d), 2):
                temp = [a, 2 * a * d[j], c - (d[j + 1]) ** 2]
                try:
                    root = (-temp[1] + math.sqrt((temp[1]) ** 2 - 4 * temp[0] * c)) / (
                        2 * temp[0]
                    )
                    roots.append(-d[j] / root)
                except (ZeroDivisionError, ValueError) as e:
                    print(f"Failed to calculate a root: {e}")
        i += 3
    return roots


if __name__ == "__main__":
    main()