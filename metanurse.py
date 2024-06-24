import sys

def get_action(observations):
    # Parse the observations
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:47]

    # Vital sign indices
    MeasuredHeartRate, MeasuredRespRate, MeasuredCapillaryGlucose, MeasuredTemperature, MeasuredMAP, MeasuredSats, MeasuredResps = range(7)
    HeartRate, RespRate, CapillaryGlucose, Temperature, MAP, Sats, Resps = range(7)

    # Extract values if measured recently
    heart_rate = vital_signs_values[HeartRate] if vital_signs_time[MeasuredHeartRate] > 0 else None
    resp_rate = vital_signs_values[RespRate] if vital_signs_time[MeasuredRespRate] > 0 else None
    map_value = vital_signs_values[MAP] if vital_signs_time[MeasuredMAP] > 0 else None
    sats = vital_signs_values[Sats] if vital_signs_time[MeasuredSats] > 0 else None

    # Check critical conditions
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression

    # Check full stabilization
    if (sats is not None and sats >= 88 
        and resp_rate is not None and resp_rate >= 8 
        and map_value is not None and map_value >= 60):
        return 48  # Finish

    # ABCDE assessment
    if events[3] == 0:  # AirwayClear
        return 3  # ExamineAirway
    if sats is None:
        return 25  # UseSatsProbe
    if resp_rate is None:
        return 4  # ExamineBreathing
    if map_value is None:
        return 27  # UseBloodPressureCuff

    return 0  # DoNothing

for step in range(350):
    observations = list(map(float, input().strip().split()))
    action = get_action(observations)
    print(action)
    if action == 48:
        break