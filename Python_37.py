```
def check():
    nums = list(map(int, input("Enter even and odd numbers (space separated): ").split()))
    print(sorted([num for num in nums if num % 2 == 0]))