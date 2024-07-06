def double_the_difference(lst):
    return sum(i**2 for i in lst if isinstance(i, int) and i >= 0 and i % 2 != 0)

input_list = input("Enter the list elements separated by space: ").split()
output = double_the_difference([int(i) for i in input_list])
print(output)