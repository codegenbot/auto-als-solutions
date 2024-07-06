```
import re

def fix_spaces():
    text = input("Enter a string: ")
    while "--" in text or "---" in text or "----" in text:
        text = text.replace("--", "- ")
        text = text.replace("---", "- -")
        text = text.replace("----", "-   ")
    return re.sub(' +', '_', text)

print(fix_spaces())