```
def sum_squares(lst):
    total = 0
    for i in range(len(lst)):
        if (i+1) % 3 == 0:
            total += lst[i] ** 2
        elif (i+1) % 4 == 0 and not (i+1) % 3 == 0:
            total += lst[i] ** 3
    return total

if __name__ == "__main__":
    input_lst = list(map(int, input("Enter numbers separated by space: ").split()))
    result = sum_squares(input_lst)
    print(f"Sum of squares: {result}")