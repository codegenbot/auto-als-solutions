from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    while True:
        try:
            input_values = list(
                map(
                    int,
                    input("Enter space-separated integers (or 'q' to quit): ").split(),
                )
            )
            return [value for value in input_values if isinstance(value, int)]
        except ValueError:
            if input("Type 'q' to quit: ") == "q":
                break