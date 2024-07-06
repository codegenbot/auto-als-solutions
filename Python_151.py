```
def double_the_difference():
    lst = []
    while True:
        num = input("Enter a number (or 'stop' to finish): ")
        if num.lower() == 'stop':
            break
        try:
            num = int(num)
            lst.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return sum(i**2 for i in lst if isinstance(i, int) and i % 2 != 0)

print(double_the_difference())