def fix_spaces(text):
    while "--" in text or "---" in text:
        text = text.replace("-", " - ")
    return text.replace(" ", "_")