```
def main():
    num_coefficients = int(input("Enter number of coefficients: "))
    xs = [int(i) for i in input(f"Enter {num_coefficients//2} coefficients (space separated): ").split()]
    
    try:
        print(find_zero(xs))
    except ValueError as e:
        print(e)

def find_zero(xs):
    if len(xs) < 2:
        raise ValueError("xs must have at least two coefficients")
    x = -sum(coeff for i, coeff in enumerate(xs) if i % 2 == 1) / sum(
        coeff for i, coeff in enumerate(xs) if i % 2 == 0
    )
    return round(x, 2)

if __name__ == "__main__":
    main()