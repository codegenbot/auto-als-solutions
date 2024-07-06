from typing import List


def all_prefixes(*strings: str) -> List[List[str]]:
    return [[string[:i] for i in range(1, len(string) + 1)] for string in strings]