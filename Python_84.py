```
def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    binary = bin(N)[2:]
    return "".join("0" if c == "1" else "1" for c in binary)