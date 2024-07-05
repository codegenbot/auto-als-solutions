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
    a, b = map(int, input("Enter two integers: ").split())
    print(gcd(a, b))
    
    text = input("Enter text: ").strip()
    target = input("Enter target: ").strip()
    print(substring_indices(text, target))