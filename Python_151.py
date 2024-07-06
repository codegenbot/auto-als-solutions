def double_the_difference(lst):
    return sum(i**2 for i in lst if isinstance(i, int) and i >= 0 and i % 2 != 0)

numbers = input("Enter a list of numbers separated by space: ").split()
double_the_difference([int(num) for num in numbers])