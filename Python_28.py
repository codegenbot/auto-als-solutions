```
from typing import List


def concatenate(strings: List[str]) -> str:
    result = "".join([s for s in strings if isinstance(s, str)])
    return result