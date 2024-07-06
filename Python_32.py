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

    while True:
        response = input("Do you want to find the zero? (y/n): ")
        if response.lower() == "y":
            try:
                print(find_zero(xs))
                break
            except ValueError as e:
                print(e)
        elif response.lower() == "n":
            print("Program ended.")
            exit()
        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()