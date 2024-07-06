import re

def fix_spaces(text):
    text = text.replace("--", "- ")
    text = text.replace("---", "- -")
    text = text.replace("----", "-   ")
    return re.sub(' +', '_', text)

text = input("Please enter your text: ")
print(fix_spaces(text))