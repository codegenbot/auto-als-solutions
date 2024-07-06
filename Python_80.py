def """Given a string s which represents an array of strings where each string has exactly 3 characters. Return whether it's possible to rearrange these substrings into an array of unique strings. The function should return True if it's possible and False otherwise..""".split("\n")[0]:
    if len(s) < 6:
        return False
    seen = set()
    for i in range(0, len(s)-2, 3):
        substr = s[i:i+3]
        if substr in seen:
            return False
        seen.add(substr)
    return True