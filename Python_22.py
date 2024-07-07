```
from typing import List


def filter_integers() -> List[int]:
    values = []
    while True:
        user_input = input("Enter a value (or 'stop' to finish): ")
        if user_input.lower() == "stop":
            break
        try:
            value = int(user_input)
            values.append(value)
        except ValueError:
            print(f"Invalid input! Please enter an integer.")
    while True:
        desired_output = input("Enter 'even' or 'odd' to filter: ").lower()
        if desired_output in ["even", "odd"]:
            break
        else:
            print("Invalid filter choice! Please enter 'even' or 'odd'.")
    if desired_output == "even":
        result = [x for x in values if x % 2 == 0]
    elif desired_output == "odd":
        result = [x for x in values if x % 2 != 0]
    else:
        result = values
    return result


print(filter_integers())