Here's the modified code:

```
def is_equal_to_sum_even(n):
    for a in range(2, n+1, 2):
        for b in range(a+2, n+1, 2):
            if a + b == n:
                return True
    return False