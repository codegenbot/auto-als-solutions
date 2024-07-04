def find_pair():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())

    seen = {}
    for num in arr:
        if target - num in seen:
            print(target - num)
            print(num)
            return
        seen[num] = True


find_pair()