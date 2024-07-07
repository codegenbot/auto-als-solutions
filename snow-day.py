def snow_day(hours, snow_ground, rate_of_snowfall, proportion_melting):
    return snow_ground + (rate_of_snowfall * hours) - (proportion_melting * hours)