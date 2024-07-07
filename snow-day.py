Here is the solution:

def snow_day(hours, initial_snow, snow_fall_rate, melting_rate):
    return initial_snow + (hours * snow_fall_rate - hours * initial_snow * melting_rate)