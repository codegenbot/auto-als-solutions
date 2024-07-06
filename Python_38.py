```
def decode_cyclic(s: str):
    """This function takes an input string and returns the decoded cyclic string."""
    result = ""
    while len(s) > 0:
        if len(s) >= 2:
            result += s[1] + s[0]
            s = s[2:]
        result += s[0]
        s = s[1:]
    return result