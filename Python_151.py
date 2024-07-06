```
def double_the_difference():
    lst = list(map(int, input("Enter a space-separated list of numbers: ").split()))
    print(sum(i**2 for i in lst if isinstance(i, int) and i >= 0 and i % 2 != 0))