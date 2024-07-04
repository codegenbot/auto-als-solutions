def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    return leaders[::-1]


if __name__ == "__main__":
    n = int(input().strip())
    if n == 0:
        print(0)
    else:
        arr = list(map(int, input().strip().split()))
        result = find_leaders(arr)
        print(len(result))
        print(" ".join(map(str, result)))