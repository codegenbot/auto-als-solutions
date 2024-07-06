def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    result = ""
    while N > 0:
        result = str(N % 2) + result
        N //= 2
    return result