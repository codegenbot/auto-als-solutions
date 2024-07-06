def sum_squares():
    lst = [i if i.isdigit() else 0 for i in input("Enter numbers separated by space: ").split()]
    total_sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            total_sum += int(lst[i]) ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += int(lst[i]) ** 3
    return total_sum

print(sum_squares())