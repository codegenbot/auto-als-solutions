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
    desired_output = input("Enter 'even' or 'odd' to filter: ").lower()
    while desired_output not in ['even', 'odd']:
        print("Invalid choice. Enter 'even' or 'odd'.")
        desired_output = input("Enter 'even' or 'odd' to filter: ").lower()
    if desired_output == 'even':
        result = [x for x in values if x % 2 == 0]
    elif desired_output == 'odd':
        result = [x for x in values if x % 2 != 0]
    else:
        print("Invalid filter choice! Returning all integers.")
        result = values
    return result

print(filter_integers())