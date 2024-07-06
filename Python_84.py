def solve(N):
    return bin(N)[2:].zfill(len(bin(N)[2:]) * 2 - 2)