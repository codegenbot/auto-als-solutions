def main():
    num = int(input("Enter a positive integer: "))
    factors = factorize(num)
    print(f"The prime factorization of {num} is {factors}.")