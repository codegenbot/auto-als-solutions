def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def substring_indices(text, target):
    indices = []
    for i in range(len(text) - len(target) + 1):
        if text[i : i + len(target)] == target:
            indices.append(i)
    return indices

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    a = int(data[0])
    b = int(data[1])
    print(gcd(a, b))
    
    text = data[2]
    target = data[3]
    print(substring_indices(text, target))