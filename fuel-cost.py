```
def fuel_cost():
    total = 0
    for num in map(int, input().split()):
        total += num // 3 - 2
    return total