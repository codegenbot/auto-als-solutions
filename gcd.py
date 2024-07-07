def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def find_indices(text, target):
    indices = []
    for i in range(len(text)):
        if text[i : i + len(target)] == target:
            indices.append(i)
    return indices


n1 = int(input())
n2 = int(input())

print(gcd(n1, n2))

text = input()
target = input()

print(find_indices(text, target))