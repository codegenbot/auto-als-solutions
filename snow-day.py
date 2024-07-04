def snow_day(hours, initial_snow, snowfall_rate, melt_proportion):
    snow = initial_snow
    for _ in range(hours):
        snow += snowfall_rate
        snow -= snow * melt_proportion
    return snow


if __name__ == "__main__":
    hours = int(input())
    initial_snow = float(input())
    snowfall_rate = float(input())
    melt_proportion = float(input())
    print(snow_day(hours, initial_snow, snowfall_rate, melt_proportion))