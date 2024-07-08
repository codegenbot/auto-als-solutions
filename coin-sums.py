```
def coin_sums(cents):
    coins = [25, 10, 5, 1]
    result = [0, 0, 0, 0]

    for coin in coins:
        while cents >= coin:
            result[coins.index(coin)] += 1
            cents -= coin

    return result

cents = int(input())
print(*coin_sums(cents))