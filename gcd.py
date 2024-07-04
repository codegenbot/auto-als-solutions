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


# Read input
a = int(input())
b = int(input())
print(gcd(a, b))

# Read input for substring indices
text = input().strip()
target = input().strip()
print(find_substring_indices(text, target))