def main():
    num = int(input("Enter a number: "))
    factors = factorize(num)
    print(f"The factors of {num} are: {factors}")


if __name__ == "__main__":
    main()