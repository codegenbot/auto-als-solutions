def sort_even_odd(even, odd):
    even.sort()
    odd.sort()
    return sorted(even + odd)