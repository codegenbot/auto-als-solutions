```python
def sort_even_odd(even_numbers, odd_numbers):
    def sort_even_odd(even_numbers, odd_numbers):
        result = [i if i % 2 == 0 else next(j) for i, j in zip(even_numbers, iter(odd_numbers))]
        return result

# Example usage:
even_numbers = [1, 4, 6, 8]
odd_numbers = [3, 5, 7]

print(sort_even_odd(even_numbers, odd_numbers))