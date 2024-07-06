def fix_spaces(text):
    while "--" in text or "---" in text or "-" * 4 in text:
        text = text.replace("--", "- ")
        text = text.replace("---", "- -")
        text = text.replace("-", " - ") if len(text) >= 1 and text[0] == "-" else text
    return text.replace(" ", "_")