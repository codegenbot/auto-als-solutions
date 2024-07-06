```
def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    binary = bin(N)[2:]
    if N % 2 == 0:
        return "Even number"
    else:
        return "Odd number"