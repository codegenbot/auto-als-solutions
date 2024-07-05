```
def check():
    numbers = list(map(int, input("Enter even and odd numbers (space separated): ").split()))
    print(sorted(numbers))

# Test the function
check()