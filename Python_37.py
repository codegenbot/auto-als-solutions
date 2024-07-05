def sort_even_odd(even, odd):
    even.sort()
    odd.sort()
    return odd + even

even_numbers = [1, 2, 3, 4, 5]
odd_numbers = [6, 7, 8, 9, 10]

print(sort_even_odd(even_numbers, odd_numbers))