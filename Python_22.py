```
from typing import List

def filter_integers() -> List[int]:
    values = []
    while True:
        user_input = input("Enter a value (or 'stop' to finish): ")
        if user_input.lower() == 'stop':
            break
        try:
            value = int(input("Enter an integer: "))
            values.append(value)
        except ValueError:
            print(f"Invalid input '{user_input}'! Please enter an integer.")
    desired_output = input("Enter 'even' or 'odd' to filter: ")
    if desired_output.lower() in ['even', 'odd']:
        result = [x for x in values if (desired_output.lower() == 'even' and x % 2 == 0) or (desired_output.lower() == 'odd' and x % 2 != 0)]
    else:
        print("Invalid filter choice! Returning all integers.")
        result = values
    return result

print(filter_integers())