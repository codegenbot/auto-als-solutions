def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_substring_indices(text, target):
    indices = []
    index = text.find(target)
    while index != -1:
        indices.append(index)
        index = text.find(target, index + 1)
    return indices

# Read input for GCD
a = int(input("Enter first integer for GCD: "))
b = int(input("Enter second integer for GCD: "))
print(gcd(a, b))

# Read input for substring indices
text = input("Enter the text string: ").strip()
target = input("Enter the target substring: ").strip()
print(find_substring_indices(text, target))