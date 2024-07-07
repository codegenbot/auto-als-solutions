```
def shopping_list():
    prices = list(map(float, input().split()))
    discounts = list(map(float, input().split()))

    n = len(prices)  
    total_price = sum(price * (1 - discount / 100) for price, discount in zip(prices, discounts))

    return round(total_price, 1)


print(shopping_list())