```
def sum_squares(numbers):
    try:
        lst = [int(i) for i in numbers.split()]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return None

    total_sum = 0
    squares = [num ** 2 for num in lst]
    cubes = [num ** 3 for num in lst]

    for i, (square, cube) in enumerate(zip(squares, cubes)):
        if i % 3 == 0:
            total_sum += square
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += cube

    return total_sum

numbers = input("Enter numbers separated by space: ")
print(sum_squares(numbers))