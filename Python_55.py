```
def find_max_value():
    max_value = float('-inf')
    while True:
        user_input = input("Enter a number (or 'stop' to finish): ")
        if user_input.lower() == 'stop':
            break
        try:
            num = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        if num > max_value:
            max_value = num
    return max_value