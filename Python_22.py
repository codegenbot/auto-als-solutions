```python
from typing import List, Any
def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

user_input = input("Enter values separated by commas: ")
values_list = [value.strip() for value in user_input.split(",")]
filtered_values = filter_integers(values_list)
print(filtered_values)