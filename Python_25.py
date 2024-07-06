def main():
    num = int(input("Enter a number to factorize: "))
    factors = factorize(num)
    print(f"The factors of {num} are {factors}.")