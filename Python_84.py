def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    rev_binary = str(bin(N)[2:])[::-1]
    return rev_binary