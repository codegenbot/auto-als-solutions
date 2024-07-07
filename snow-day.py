def snow_day(hours, snow_ground, rate_of_snowfall, proportion_melting):
    for _ in range(hours):
        snow_ground += rate_of_snowfall
        snow_ground *= (1 - proportion_melting)
    return round(snow_ground, 8)