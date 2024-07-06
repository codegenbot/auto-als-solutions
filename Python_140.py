```
def fix_spaces(text):
    text = text.strip().replace("--", "- ").replace("---", "- -").replace("----", "-   ")
    return text.replace(" ", "_")