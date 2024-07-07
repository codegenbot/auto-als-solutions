```
from typing import List

def filter_integers() -> List[int]:
    values = []
    while True:
        user_input = input("Enter a value (or 'stop' to finish): ")
        if user_input.lower() == 'stop':
            break
        try:
            value = int(user_input)
            # add validation for your range here, e.g., 1-100
            if not 1 <= value <= 100: 
                print(f"Invalid input '{user_input}'! Please enter an integer between 1 and 100.")
                continue
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