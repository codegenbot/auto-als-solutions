def total_price_after_discount(prices, discounts):
    total_price = sum(
        price * (1 - discount / 100) for price, discount in zip(prices, discounts)
    )
    return total_price

if __name__ == "__main__":
    n_prices = int(input().strip())
    prices = list(map(float, input().strip().split()))
    n_discounts = int(input().strip())
    discounts = list(map(float, input().strip().split()))

    result = total_price_after_discount(prices, discounts)
    print(f"{result:.2f}")