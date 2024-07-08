```
def coin_sums(cents):
    coins = [25, 10, 5, 1]  # quarters, dimes, nickles, pennies
    result = []

    while cents > 0:
        for coin in coins[::-1]:  
            count = min(cents // coin, len(result))
            result.extend([coin] * count)
            cents -= coin * count
            if cents == 0: break

    return result


cents = int(input())
print(*coin_sums(cents))