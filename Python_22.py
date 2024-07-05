from typing import List, Any
def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

user_input = input("Enter values separated by commas: ")
values_list = user_input.split(",")
filtered_values = list(map(lambda x: int(x) if x.isdigit() else 0, values_list))
print(filtered_values)