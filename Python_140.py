def fix_spaces():
    text = input("Enter your text: ")
    while "--" in text or "---" in text or "----" in text:
        text = text.replace("--", "- ")
        text = text.replace("---", "- -")
        text = text.replace("----", "-   ")
    return text.replace(" ", "_")