```
def double_the_difference():
    lst = input("Enter numbers separated by space: ").split()
    try:
        numbers = [int(i) for i in lst]
        odd_sum = sum(i for i in numbers if i % 2 != 0)
        
        if not all(i > 0 for i in numbers):
            return "Program did not receive expected input"
        
        result = abs(sum(i**2 for i in numbers) - (2 * odd_sum))
        return result
    except ValueError:
        return "Invalid input"

print(double_the_difference())