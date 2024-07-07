def shopping_list():
    n = int(input())
    prices = [float(x) for x in input().split()]
    discount_rates = [float(x) / 100 for x in input().split()]

    total_price = sum(
        [price - (price * rate) for price, rate in zip(prices, discount_rates)]
    )

    return total_price