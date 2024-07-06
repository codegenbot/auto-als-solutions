```
def solve(N):
    return bin((1 << len(bin(N)[2:])) + N)[2:]