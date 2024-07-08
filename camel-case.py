```
import re

def camel_case(s):
    return "".join(
        word.capitalize() if i > 0 else word.strip("-").lower()
        for i, word in enumerate(map(str, re.split("-(?=[a-z])", s)))
    )