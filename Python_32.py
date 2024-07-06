import math


def find_zero(coeffs):
    roots = []
    for i in range(0, len(coeffs), 2):
        temp = [coeffs[i], coeffs[i + 1]]
        try:
            root = (-temp[1] + math.sqrt(temp[1] ** 2 - 4 * temp[0])) / (2 * temp[0])
            roots.append(-temp[1] / (2 * root))
        except (ZeroDivisionError, ValueError) as e:
            print(f"Failed to calculate a root: {e}")
    return roots


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

    coeffs = [
        int(coeff)
        for coeff in (input("Enter coefficients (space separated): ") + " ").split()
    ]
    while len(coeffs) % 2 != 0:
        if num_coefficients == len(coeffs):
            raise ValueError("coeffs must have even number of coefficients")
        new_coeff = input(f"Add more coefficients: ")
        coeffs += [int(coeff) for coeff in new_coeff.split()]

    if len(coeffs) < 2:
        raise ValueError("coeffs must have at least two coefficients")

    try:
        print(find_zero(coeffs))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()