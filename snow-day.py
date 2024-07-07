```
def snow_day(hours, initial_amount, rate, melt_rate):
    return round(initial_amount + (rate * hours) - (melt_rate * hours), 6)