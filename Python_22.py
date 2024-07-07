```
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

if __name__ == "__main__":
    user_input = input("Please enter a list of values separated by comma (e.g., 1,2,3): ")
    try:
        values = [int(i) for i in user_input.split(',')]
        print(filter_integers(values))
    except ValueError:
        print("Invalid input. Please ensure all values are integers.")