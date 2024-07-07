Here's the solution for the GCD and Indices of Substring problems:

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def indices_of_substring(text, target):
    result = []
    last_index = 0
    while True:
        pos = text.find(target, last_index)
        if pos == -1:
            break
        result.append(pos + 1)
        last_index = pos + 1
    return result