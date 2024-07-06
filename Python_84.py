```
def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    return bin(N)[2:]