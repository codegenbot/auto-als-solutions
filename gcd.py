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
    mode = input("Enter mode (gcd/substring): ").strip()
    
    if mode == "gcd":
        try:
            a, b = map(int, input("Enter two integers: ").split())
            print(gcd(a, b))
        except ValueError:
            print("Please provide exactly two integers separated by space.")
    elif mode == "substring":
        text = input("Enter the text string: ").strip()
        target = input("Enter the target string: ").strip()
        print(substring_indices(text, target))
    else:
        print("Invalid mode. Please enter 'gcd' or 'substring'.")