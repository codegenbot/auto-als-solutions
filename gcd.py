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
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    try:
        a, b = map(int, data[0].split())
        print(gcd(a, b))
    except (ValueError, IndexError):
        print("Please provide exactly two integers separated by space.")
    
    if len(data) > 2:
        text = data[1].strip()
        target = data[2].strip()
        print(substring_indices(text, target))
    else:
        print("Please provide both text and target strings.")