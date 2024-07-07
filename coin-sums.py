def coin_sums(cents):
    coins = [25, 10, 5, 1]
    results = []
    for i in range((cents // 25) + 1):
        remaining_cents = cents - i * 25
        quarters = i
        nickles = remaining_cents // 5
        dimes = (remaining_cents % 5) // 1
        pennies = remaining_cents % 1
        results.append([quarters, nickles, dimes, pennies])
    return min(results)


cents = int(input())
print(*coin_sums(cents))