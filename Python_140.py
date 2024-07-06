```
def fix_spaces(text):
    while True:
        if "--" in text:
            text = text.replace("--", "- ")
        elif "---" in text:
            text = text.replace("---", "- -")
        elif "----" in text:
            text = text.replace("----", "-   ")
        else:
            break
    return text.replace(" ", "_")