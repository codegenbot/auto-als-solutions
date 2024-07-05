def sort_even_odd(even, odd):
    even.sort()
    odd.sort()
    return odd + even

even_numbers = [4, 2, 6, 1]
odd_numbers = [3, 7, 5, 10]

print(sort_even_odd(even_numbers, odd_numbers))