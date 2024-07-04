def coin_sums(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents
    return pennies, nickels, dimes, quarters


if __name__ == "__main__":
    cents = int(input())
    pennies, nickels, dimes, quarters = coin_sums(cents)
    print(pennies)
    print(nickels)
    print(dimes)
    print(quarters)