def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    return f"0b{bin(N)[2:]}")