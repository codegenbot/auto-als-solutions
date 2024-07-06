```
def solve(N):
    fib = [0, 1]
    total = 0
    while True:
        next_fib = fib[-1] + fib[-2]
        if len(str(next_fib)) > N:
            break
        if next_fib % 3 != 0:
            total += next_fib
        fib.append(next_fib)
    return total