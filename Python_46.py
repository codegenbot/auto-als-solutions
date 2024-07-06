def fib4(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 3:
        return [0, 0, 2, 0][n]
    fib4s = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4s.append(fib4s[i - 1] + fib4s[i - 2] + fib4s[i - 3] + fib4s[i - 4])
    return fib4s[n]