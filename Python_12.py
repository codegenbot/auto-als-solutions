```
from typing import List, Optional

def longest(strings: list[str]) -> typing.Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)