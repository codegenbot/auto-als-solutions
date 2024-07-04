def first_negative_sum_index(nums):
    total = 0
    for i, num in enumerate(nums):
        total += num
        if total < 0:
            return i
    return -1


if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(first_negative_sum_index(nums))