```
def snow_day(hours, amount, rate, melt_rate):
    snow = amount
    for _ in range(hours):
        snow += rate  # add new snow
        snow -= melt_rate  # subtract melted snow
    return round(snow, 6)