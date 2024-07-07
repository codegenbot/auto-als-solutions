def snow_day(hours, initial_snow, rate_of_fall, melt_rate):
    total_snow = initial_snow
    for _ in range(hours):
        total_snow += rate_of_fall  # Add new snowfall first
        total_snow -= min(total_snow, rate_of_fall) * melt_rate  # Then subtract melted amount
    return round(total_snow, 6)