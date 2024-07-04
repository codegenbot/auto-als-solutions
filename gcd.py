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
    try:
        # Read two integers for gcd
        a, b = map(int, input("Enter two integers separated by space: ").split())
        print(gcd(a, b))

        # Read text and target for substring indices
        text = input("Enter text: ").strip()
        target = input("Enter target: ").strip()
        print(substring_indices(text, target))
    except ValueError:
        print("Error: Please ensure you provide appropriate inputs.")