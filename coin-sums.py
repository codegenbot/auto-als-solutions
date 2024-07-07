def coin_sums():
    cents = int(input())
    coins = [25, 10, 5, 1]
    pennies = cents
    quarters = pennies // 25
    pennies %= 25
    dimes = pennies // 10
    pennies %= 10
    nickles = pennies // 5
    pennies %= 5
    print(quarters)
    print(nickles)
    print(dimes)
    print(pennies)


coin_sums()