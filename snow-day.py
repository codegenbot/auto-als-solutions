def snow_day(hours, snow_ground, rate_of_snowfall, melting_rate):
    for _ in range(hours):
        snow_ground += rate_of_snowfall
        snow_ground -= min(snow_ground, snow_ground * melting_rate)
    return round(snow_ground, 8)