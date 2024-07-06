def double_the_difference(lst):
    return sum(i**2 for i in lst if isinstance(i, int) and i >= 0 and i % 2 != 0)

numbers = input("Enter numbers separated by space: ")
numbers = [int(num) for num in numbers.split()]
print(double_the_difference(numbers))