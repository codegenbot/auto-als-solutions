from typing import List

def filter_integers() -> List[int]:
    values = []
    while True:
        user_input = input("Enter a value (or 'stop' to finish): ")
        if user_input.lower() == 'stop':
            break
        if not user_input.isnumeric():
            print(f"Invalid input '{user_input}'! Please enter an integer.")
        else:
            values.append(int(user_input))
    return values

print(filter_integers())