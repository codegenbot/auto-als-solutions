prices = list(map(float, input().split()[1:]))
discounts = list(map(float, input().split()[1:]))

total_price = sum(p * (1 - d / 100) for p, d in zip(prices, discounts))
print(total_price)