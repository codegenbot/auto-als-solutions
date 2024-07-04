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

# Read all input first
inputs = [input().strip() for _ in range(4)]
a = int(inputs[0])
b = int(inputs[1])
text = inputs[2]
target = inputs[3]

# Execute the functions
print(gcd(a, b))
print(find_substring_indices(text, target))