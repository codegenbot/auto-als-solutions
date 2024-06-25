airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False

while True:
    try:
        input_obs = input().strip().split()
        observations = [float(x) for x in input_obs[:39]]
        times = [float(x) for x in input_obs[39:46]]
        measurements = [float(x) for x in inputoll[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
            print(17)  # Start Chest Compression
            continue

        if not airway_checked:
            print(3)  # ExamineAirway
            airway_checked = True
            airway_clear = observations[3] > 0.1
            continue

        if sats is not None and sats < 88:
            print(30)  # Use Non-Rebreather Mask
            continue
        elif map_value is not None and map_value < 60:
            print(15)  # Give Fluids
            circulation_assessed = True
            continue

        if all([airway_checked, airway_clear, sats and sats >= 88, map_value and map_value >= 60, resp_rate and resp_rate >= 8]):
            print(48)  # Finish
            break

        print(0)  # No specific action needed now

    except EOFError:
        break