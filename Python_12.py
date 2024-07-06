from typing import List, Optional


def longest_strings(strings: List[str]) -> Optional[List[str]]:
    if not strings:
        return None
    max_len = len(max(strings, key=len))
    return [s for s in strings if len(s) == max_len]