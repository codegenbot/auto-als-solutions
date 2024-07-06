```Python
def sum_squares(numbers):
    try:
        lst = [int(i) for i in numbers.split() if i.isdigit()]
    except ValueError:
        print("Invalid input. Please enter only numbers and spaces.")
        return None

    total_sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            total_sum += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += lst[i] ** 3
    return total_sum


numbers = input("Enter numbers separated by space: ")
print(sum_squares(numbers))