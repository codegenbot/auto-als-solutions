def double_the_difference(lst):
    return sum(i**2 for i in lst if isinstance(i, int) and i >= 0 and i % 2 != 0)

input_list = list(map(int, input("Enter the numbers separated by space: ").split()))
output = double_the_difference(input_list)
print(output)