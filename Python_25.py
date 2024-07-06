def find_max_factor(n: int) -> int:
    max_factor = 1
    for i in range(2, n + 1):
        if n % i == 0 and i > max_factor:
            max_factor = i
    return max_factor