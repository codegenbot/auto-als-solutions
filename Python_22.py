```
from typing import List, Any

def filter_integers() -> List[int]:
    values = []
    while True:
        user_input = input("Enter a value (or 'stop' to finish): ")
        if user_input.lower() == 'stop':
            break
        try:
            value = int(user_input)
            values.append(value)
        except ValueError:
            print(f"Invalid input '{user_input}'! Please enter an integer.")
    return values

print(filter_integers())