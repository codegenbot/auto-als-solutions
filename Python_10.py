```
def make_palindrome(string: str) -> str:
    s = string.lower()
    for i in range(len(s), 0, -1):
        if s[:i] == s[:i][::-1]:
            if string.islower():
                return string + s[:i][::-1]
            else:
                return string + s[:i][::-1].capitalize()