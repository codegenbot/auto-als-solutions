```
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def indices_of_substring(text, target):
    result = []
    i = 0
    while i <= len(text) - len(target):
        pos = text.find(target)
        if pos != -1:
            result.append(i + pos)
            i += pos + 1
        else:
            break
    return result

# Testing the functions
a, b = int(input()), int(input())
print(gcd(a, b))
text, target = input(), input()
print(indices_of_substring(text, target))