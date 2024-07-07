```
def fuel_cost():
    total = 0
    for line in sys.stdin:
        if line: 
            num = int(line.strip())
            total += num // 3 - 2
    return total