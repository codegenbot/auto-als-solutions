def coin_sums():
    cents = int(input())
    coins = [25, 10, 5, 1]
    quarters = cents // 25
    cents %= 25
    nickles = cents // 5
    cents %= 5
    dimes = cents // 10
    cents %= 10
    pennies = cents
    print(quarters)
    print(nickles)
    print(dimes)
    print(pennies)

coin_sums()