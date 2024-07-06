def fix_spaces(text):
    return (
        text.replace(" ", "_")
        .replace("  +", lambda x: "-" + x.group().lstrip())
        .replace("   ", lambda x: "-_" + x.group().lstrip())
    )