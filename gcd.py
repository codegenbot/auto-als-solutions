def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def substring_indices(text, target):
    indices = []
    for i in range(len(text) - len(target) + 1):
        if text[i: i + len(target)] == target:
            indices.append(i)
    return indices

if __name__ == "__main__":
    # Read two integers for gcd
    a, b = map(int, input().split())
    print(gcd(a, b))

    # Read text and target for substring indices
    text = input().strip()
    target = input().strip()
    print(substring_indices(text, target))