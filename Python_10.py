def make_palindrome(string: str) -> str:
    for i in range(len(string)):
        for j in range(i+1):
            substr = string[j:i+1] + string[i::-1]
            if len(substr) <= 10:
                return substr
    return ""