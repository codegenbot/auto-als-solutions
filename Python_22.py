from typing import List, Any
def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

user_input = input("Enter values separated by commas: ")
values_list = user_input.split(",")
filtered_values = [int(value) if value else 0 for value in values_list]
print(filtered_values)