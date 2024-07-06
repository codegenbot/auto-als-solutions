def double_the_difference():
    lst = input("Enter numbers separated by space: ").split()
    try:
        if len(lst) == 0:
            return "Invalid input"
        odd_sum = sum(int(i) for i in lst if int(i) % 2 != 0)
        return abs(sum(int(i)**2 for i in lst if int(i) > 0) - (2 * odd_sum))
    except ValueError:
        return "Invalid input"

print(double_the_difference())