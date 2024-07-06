```
def sum_squares(lst):
    total_sum = 0
    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 != 0:
            total_sum += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += lst[i] ** 3
    return total_sum

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = [int(i) for i in input("Enter the elements of the list: ").split()]
    print(sum_squares(lst))

if __name__ == "__main__":
    main()