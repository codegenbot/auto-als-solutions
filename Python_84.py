def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    return format(int(N), 'b')