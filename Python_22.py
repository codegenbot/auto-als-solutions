from typing import List


def filter_integers() -> List[int]:
    values = []
    value_input = input("Enter the first integer: ")
    try:
        values.append(int(value_input))
    except ValueError:
        print(f"Invalid input '{value_input}'! Please enter an integer.")
    while True:
        user_input = input("Enter a value (or 'stop' to finish): ")
        if user_input.lower() == "stop":
            break
        try:
            value = int(input("Enter an integer: "))
            values.append(value)
        except ValueError:
            print(f"Invalid input '{user_input}'! Please enter an integer.")
    filter_choice = input("Enter 'even' or 'odd' to filter: ")
    if filter_choice.lower() in ["even", "odd"]:
        result = [
            x
            for x in values
            if (filter_choice.lower() == "even" and x % 2 == 0)
            or (filter_choice.lower() == "odd" and x % 2 != 0)
        ]
    else:
        print("Invalid filter choice! Returning all integers.")
        result = values
    return result


print(filter_integers())