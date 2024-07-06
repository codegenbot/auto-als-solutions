from typing import List, Union


def concatenate(strings: Union[List[str], str]) -> str:
    result = ""
    if isinstance(strings, list):
        for s in strings:
            result += s
    else:
        result = strings
    return result