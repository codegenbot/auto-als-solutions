def solve(N):
    if N < 0:
        return "Error: Input must be a non-negative integer"
    elif not isinstance(N, int):
        return "Error: Input must be an integer"
    return format(abs(int(N)), 'b')