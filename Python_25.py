def main():
    num = int(input("Enter a positive integer: "))
    factors = factorize(num)
    if len(factors) == 1:
        print(f"{num} is a prime number.")
    else:
        print(f"The factors of {num} are: {factors}.")


if __name__ == "__main__":
    main()