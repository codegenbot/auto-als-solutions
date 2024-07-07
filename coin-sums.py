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
    print(f"Quarters: {quarters}")
    print(f"Nickels: {nickles}")
    print(f"Dimes: {dimes}")
    print(f"Pennies: {pennies}")