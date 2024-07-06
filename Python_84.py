def solve(N):
    N += 1
    count = 0
    while (1 << count) <= N:
        count += 1
    return str(bin(N))[2:].zfill(count)