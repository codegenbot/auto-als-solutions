def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    binary = ""
    for i in range(1, N + 1):
        if N % i == 0:
            binary += str(i) + " "
    return binary.strip()