import re

def fix_spaces(text):
    text = text.replace("--", "- ")
    text = text.replace("---", "- -")
    text = text.replace("----", "-   ")
    return re.sub(' +', '_', text)

while True:
    text = input("Enter your text: ")
    if text:  
        print(fix_spaces(text))
        break 