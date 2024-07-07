```
def fuel_cost():
    total = 0
    for line in sys.stdin:
        total += int(line) // 3 - 2
    return total