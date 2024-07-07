```
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(1, 1))
print(indices_of_substring("Hello World", "World"))
print(gcd(4, 400000))
print(indices_of_substring("bananaana", "ana"))
print(gcd(54, 24))
print(indices_of_substring("abcdefg", "def"))
print(gcd(4200, 3528))
print(indices_of_substring("HelloWorldHelloWorld", "Hello"))
print(gcd(820000, 63550))