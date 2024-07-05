def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def substring_indices(text, target):
    indices = []
    i = text.find(target)
    while i != -1:
        indices.append(i)
        i = text.find(target, i + 1)
    return indices

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    a, b = int(data[0]), int(data[1])
    print(gcd(a, b))
    
    text = data[2]
    target = data[3]
    print(substring_indices(text, target))