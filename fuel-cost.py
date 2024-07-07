def fuel_cost():
    total = 0
    for line in iter(input, ""):
        total += int(line) // 3 - 2
    return total