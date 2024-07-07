def gcd(a, b):
    if a == 0 or b == 0:
        return abs(a)
    while b != 0:
        a, b = b, a % b
    return abs(a)

def indices_of_substring(text, target):
    result = []
    i = 0
    while i < len(text):
        pos = text.find(target)
        if pos == -1:
            break
        result.append(pos + 1)
        i += 1
    return result