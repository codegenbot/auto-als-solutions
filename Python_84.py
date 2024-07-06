```
def solve(N):
    return format(int(sum(int(i) for i in str(bin(N)[2:]))), '04b')