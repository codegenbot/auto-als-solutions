```
numbers = ' '.join(str(i) for i in input("Enter numbers separated by space: ").split())
print(sum_squares(numbers))
def sum_squares(numbers):
    lst = [int(i) for i in numbers.split()]
    total_sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            total_sum += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += lst[i] ** 3
    return total_sum