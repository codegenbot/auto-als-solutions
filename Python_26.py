```
from typing import List

def remove_duplicates(lst: List[int]) -> List[int]:
    return sorted(list(set(lst)))