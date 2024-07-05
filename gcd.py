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
    try:
        a, b = map(int, input("Enter two integers: ").split())
        print(gcd(a, b))
    except ValueError:
        print("Please enter two valid integers.")
    
    # Read text and target for substring indices
    text = input("Enter the text: ").strip()
    target = input("Enter the target: ").strip()
    print(substring_indices(text, target))