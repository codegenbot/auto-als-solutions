```
import re
def fix_spaces():
    text = input("Enter your text: ")
    text = text.replace("--", "- ")
    text = text.replace("---", "- -")
    text = text.replace("----", "-   ")
    return re.sub('[\s]+', '_', text)

print(fix_spaces())