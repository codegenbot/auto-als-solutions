def solve(N):
    total = 0
    for i in bin(N)[2:]:
        total += int(i)
    return str(total) if N > 1 else str(total)