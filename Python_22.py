```
from typing import List, Any
def filter_integers(values: List[Any]) -> List[int]:
    return [int(value) for value in values if isinstance(value, str) and value.isdigit()]

user_input = input("Enter values separated by commas: ")
values_list = user_input.split(",")
filtered_values = filter_integers(values_list)
print(filtered_values)