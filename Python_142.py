```python
def sum_squares(lst):
    total = 0
    for num in lst:
        if (lst.index(num) + 1) % 3 == 0:
            total += num ** 2
        elif (lst.index(num) + 1) % 4 == 0 and not (lst.index(num) + 1) % 3 == 0:
            total += num ** 3
    return total

if __name__ == "__main__":
    input_lst = list(map(int, input("Enter numbers separated by space: ").split()))
    result = sum_squares(input_lst)
    print(f"Sum of squares: {result}")