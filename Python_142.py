```
def sum_squares(numbers):
    try:
        lst = [int(i) for i in numbers.split()]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return None

    total_sum = 0
    for i, num in enumerate(lst):
        if (i+1) % 3 == 0:
            total_sum += num ** 2
        elif (i+1) % 4 == 0 and (i+1) % 3 != 0:
            total_sum += num ** 3
    return total_sum

numbers = input("Enter numbers separated by space: ")
print(sum_squares(numbers))