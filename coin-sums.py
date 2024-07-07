def coin_sums(cents):
    coins = [25, 10, 5, 1]
    coin_counts = [0] * 4

    for i in range(3, -1, -1):
        count = min(cents // coins[i], 99) if i == 2 else cents // coins[i]
        coin_counts[i] = count
        cents %= coins[i]

    return str(coin_counts[0]) + "\n" + " ".join(map(str, coin_counts[1:]))