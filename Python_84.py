```
def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    binary = bin(N)[2:]
    return ''.join('1' if c == '0' else c for c in binary)