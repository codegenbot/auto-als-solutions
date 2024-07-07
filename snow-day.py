def snow_day(hours, amount, rate, melt_rate):
    snow = amount
    for _ in range(hours):
        snow += rate  
        snow -= melt_rate  
    return round(snow, 6)