```
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def indices_of_substring(text, target):
    result = []
    i = 0
    while i < len(text):
        pos = text.find(target, i)
        if pos != -1:
            result.append(pos + 1)
            i = pos + 1
        else:
            break
    return result

print(gcd(1, 1))
print(indices_of_substring("Hello World", "World"))
print(gcd(4, 400000))
print(indices_of_substring("bananaana", "ana"))
print(gcd(54, 24))
print(indices_of_substring("abcdefg", "def"))
print(gcd(4200, 3528))
print(indices_of_substring("HelloWorldHelloWorld", "Hello"))
print(gcd(820000, 63550))