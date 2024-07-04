def snow_day(hours, initial_snow, snowfall_rate, melt_proportion):
    snow = initial_snow
    for _ in range(hours):
        snow *= 1 - melt_proportion
        snow += snowfall_rate
        if snow < 0:
            snow = 0
    return round(snow, 15)


if __name__ == "__main__":
    hours = int(input())
    initial_snow = float(input())
    snowfall_rate = float(input())
    melt_proportion = float(input())
    print(snow_day(hours, initial_snow, snowfall_rate, melt_proportion))