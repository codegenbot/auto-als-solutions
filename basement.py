def find_first_negative_index(arr):
    current_sum = 0
    for index, value in enumerate(arr):
        current_sum += value
        if current_sum < 0:
            return index
    return -1


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_first_negative_index(arr))