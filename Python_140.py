```python
def fix_spaces(text):
    while "--" in text or "---" in text or "----" in text:
        text = text.replace("--", "- ")
        text = text.replace("---", "- -")
        text = text.replace("----", "-   ")
    return text.strip().replace(" ", "_")