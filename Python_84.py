def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    result = bin(N)[2:]
    return result.replace("1", "#").replace("0", "~")