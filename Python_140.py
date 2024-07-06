```
def fix_spaces(text):
    while "--" in text or "---" in text or "----" in text:
        text = text.replace("--", "- ")
        text = text.replace("---", "- -")
        text = text.replace("----", "-   ")
    return text.replace(" ", "_")

text = input("Enter your text: ")
print(fix_spaces(text))