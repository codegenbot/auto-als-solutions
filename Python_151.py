def check(lst, func):
    result = func([int(i) for i in input().split()])
    print(result)