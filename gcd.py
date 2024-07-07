```
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def indices_of_substring(text, target):
    result = []
    last_index = -1
    while True:
        pos = text.find(target, last_index + 1)
        if pos == -1:
            break
        result.append(pos + 1)
        last_index = pos
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