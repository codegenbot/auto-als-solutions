```python
def sum_squares(numbers):
    try:
        lst = [int(i) for i in numbers.split()]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return None

    total_sum = 0
    group_count = 0
    for num in lst:
        if group_count % 3 == 0 and group_count != 0:  
            if group_count % 12 == 0:  
                total_sum += num ** 3
            else:  
                total_sum += num ** 2
        group_count += 1

    return total_sum

numbers = input("Enter numbers separated by space: ")
print(sum_squares(numbers))