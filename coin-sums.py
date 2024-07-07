def coin_sums(cents):
    coins = [25, 10, 5, 1]
    pennies = cents // 100
    nickles = (cents % 100) // 20
    dimes = ((cents % 100) % 20) // 10
    quarters = ((cents % 100) % 20) % 10
    return pennies, nickles, dimes, quarters


c = int(input())
print(*coin_sums(c))