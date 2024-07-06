```Python
def double_the_difference(lst):
    odd_sum = sum(i for i in lst if isinstance(i, int) and i % 2 != 0)
    return abs(sum(i**2 for i in lst if isinstance(i, int) and i > 0) - (2 * odd_sum))

user_input = input("Enter a list of numbers separated by space: ")
lst = [int(i) for i in user_input.split()]
print(double_the_difference(lst))