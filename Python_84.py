```
def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    binary = bin(N)[2:]
    return binary[::-1]