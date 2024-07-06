Here is the completed code:

def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if string.islower():
        prefix = ''
    else:
        prefix = ''.join(ch for ch in string if not ch.isalnum())
    suffix = string[::-1]
    while len(suffix) > 0 and not is_palindrome(prefix + suffix):
        suffix = suffix[1:]
    return prefix + suffix