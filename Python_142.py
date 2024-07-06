```python
def sum_squares(lst):
    total = 0
    for num in lst:
        if num % 3 == 0 and num % 4 != 0:
            total += num ** 2
        elif num % 4 == 0:
            total += num ** 3
    return total

if __name__ == "__main__":
    input_lst = list(map(int, input("Enter numbers separated by space: ").split()))
    result = sum_squares(input_lst)
    print(f"Sum of squares: {result}")