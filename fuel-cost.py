```
def fuel_cost():
    total = 0
    for line in iter(input, ''):
        num = int(line)
        total += num // 3 - 2
    return total