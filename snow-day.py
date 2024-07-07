def snow_day(hours, amount, rate, melt_rate):
    total_amount = 0
    for _ in range(hours):
        total_amount += rate
        if total_amount > 0:
            melted_amount = min(total_amount * melt_rate, total_amount)
            total_amount -= melted_amount
    return round(total_amount, 5)


hours = int(input())
amount, rate, melt_rate = map(float, [input() for _ in range(3)])
print(snow_day(hours, amount, rate, melt_rate))