def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = []
    for s in strings:
        if substring in s:
            result.append(s)
    return result