```
numbers = input("Enter numbers separated by space: ").split()
try:
    numbers = [float(num) for num in numbers]
except ValueError:
    print("Invalid input")
    exit()

print(mean_absolute_deviation(numbers))