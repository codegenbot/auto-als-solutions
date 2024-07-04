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
        a, b = map(int, input().split())
        print(gcd(a, b))
    except ValueError:
        print("Please provide exactly two integers separated by space.")
    
    text = input().strip()
    target = input().strip()
    print(substring_indices(text, target))