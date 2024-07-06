def solve(N):
    result = []
    while N:
        result.append(str(N % 2))
        N //= 2
    return "".join(result[::-1])