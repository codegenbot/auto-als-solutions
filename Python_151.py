def double_the_difference():
    lst = input("Enter numbers separated by space: ").split()
    try:
        numbers = [int(i) for i in lst]
        odd_sum = sum(i for i in numbers if i % 2 != 0)
        return abs(sum(i**2 for i in numbers if i > 0) - (2 * odd_sum))
    except ValueError:
        return "Invalid input"
    except Exception as e:
        print(f"Error: {e}")
        return "Program did not receive expected input"

print(double_the_difference())