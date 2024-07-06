def fix_spaces(text):
    text = text.replace('   ', ' ').replace('  ', ' ').replace(' ', '_')
    return text.replace(' ', '-').rstrip('-')