Here is the completed code:

```
from typing import List
from collections import deque


def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    for group in paren_string.split():
        level = 0
        queue = deque()
        for char in group:
            if char == '(':
                queue.append(char)
            elif char == ')':
                if queue and queue[-1] == '(':
                    queue.pop()
                else:
                    level += 1
        result.append(level)
    return result