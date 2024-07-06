```
def double_the_difference(lst):
    odd_sum = sum(i for i in lst if isinstance(i, int) and i % 2 != 0)
    return abs(sum(i**2 for i in lst if isinstance(i, int) and i > 0) - (2 * odd_sum))

input_list = [int(x) for x in input("Enter space-separated integers: ").split()]
print(double_the_difference(input_list))