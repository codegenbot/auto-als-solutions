def solve(N):
    return bin(
        sum(int(x) for x in str((1 << len(bin(N)[2:]) - 1) ^ int(str(bin(N)[2:]), 2)))
    )[2:]