def coin_sums(cents):
    coins = [25, 10, 5, 1]  
    result = [0, 0, 0, 0]

    for i in range(len(coins)):
        count = 0
        while cents >= coins[i]:
            if cents < coins[i]:
                result[i] = 1
                break
            else:
                cents -= coins[i]
                count += 1
        result[i] = count

    return result


cents = int(input())
print(*coin_sums(cents))