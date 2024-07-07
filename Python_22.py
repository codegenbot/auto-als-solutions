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
    desired_output = input("Enter 'even' or 'odd' to filter: ").lower()
    while desired_output not in ["even", "odd"]:
        print("Invalid filter choice! Please enter 'even' or 'odd'.")
        desired_output = input("Enter 'even' or 'odd' to filter: ").lower()
    result = [
        x
        for x in values
        if (desired_output == "even" and x % 2 == 0)
        or (desired_output == "odd" and x % 2 != 0)
    ]
    return result


print(filter_integers())