```
def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    binary = bin(N)[2:]
    flipped_binary = "".join("1" if c == "0" else "0" for c in binary)
    return flipped_binary