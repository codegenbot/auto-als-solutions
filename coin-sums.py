def coin_sums(cents):
    coins = [25, 10, 5, 1]
    answers = [0, 0, 0, 0]

    for i in range(len(coins)):
        while cents >= coins[i]:
            cents -= coins[i]
            answers[i] += 1

    return tuple(answers)