```
def double_the_difference(lst):
    odd_sum = sum(i for i in lst if isinstance(i, int) and i % 2 != 0)
    return abs(sum(i**2 for i in lst if isinstance(i, int) and i > 0) - (2 * odd_sum))


numbers = input("Enter the list of numbers separated by spaces: ").split()
print(double_the_difference([int(num) for num in numbers]))