def is_equal_to_sum_even(n):
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if a + b == n:
                return True
    return False