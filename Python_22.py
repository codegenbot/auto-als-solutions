```
def filter_integers():
    values = []
    while True:
        user_input = input("Enter a value (or 'stop' to finish): ")
        if user_input.lower() == 'stop':
            break
        try:
            value = int(user_input)
            values.append(value)
        except ValueError:
            print(f"Invalid input! Please enter an integer.")
    desired_output = input("Enter 'even', 'odd' or 'all' to filter: ").lower()
    if desired_output not in ['even', 'odd']:
        desired_output = 'all'
    if desired_output == 'all':
        result = values
    else:
        result = [x for x in values if (desired_output == 'even' and x % 2 == 0) or (desired_output == 'odd' and x % 2 != 0)]
    return result

print(filter_integers())