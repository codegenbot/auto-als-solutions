```python
from typing import List

def filter_integers() -> None:
    result = []
    while True:
        line = input("Enter a value (or 'stop' to finish): ")
        if line.lower() == 'stop':
            break
        try:
            integer = int(line)
            result.append(integer)
        except ValueError:
            pass
    print(result)