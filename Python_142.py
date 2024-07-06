def sum_squares():
    lst = []
    while True:
        try:
            numbers = input("Enter numbers separated by space: ").split()
            lst = [int(i) for i in numbers]
            break
        except ValueError:
            print("Invalid Input. Please enter numeric values only.")

    total_sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            total_sum += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            try:
                total_sum += lst[i] ** 3
            except ValueError:
                return "Invalid Input"
    return total_sum

print(sum_squares())