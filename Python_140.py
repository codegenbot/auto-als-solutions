import re


def fix_spaces(text):
    text = text.replace("--", "- ")
    text = text.replace("---", "- -")
    text = text.replace("----", "-   ")
    return re.sub(" +", "-", text)