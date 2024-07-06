```
import re

def fix_spaces(text):
    text = text.replace("--", " -")
    while '--' in text:
        text = text.replace('--', ' -')
    return re.sub(' +', '_', text)

text = input("Enter your text: ")
print(fix_spaces(text))