airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False


def get_vitals(measurements, times):
    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    return sats, map_in_value, resp_rate


while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats, map_value, resp_rate = get_vitals(measurements, times)

        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start Chest Compression
            if sats < 65:
                print(10)  # Give Adrenaline
                continue

        if not airway_checked:
            print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0.1  # AirwayClear has significant relevance
            continue

        if airway_clear and not breathing_assessed:
            print(4)  # Examine Breathing
            breathing_assessed = True
            if events[7] > 0.1:  # BreathingNone significant relevance
                print(29)  # Use Bag Valve Mask
                continue

        if airway_clear and not circulation_assessed:
            if sats is not None and sats < 88:
                print(30)  # Use Non Rebreather Mask
            if map_value is not None and map_value < 60:
                print(15)  # Give Fluids
            circulation_assessed = True
            continue

        all_stable = all(
            [
                airway_checked,
                airpod_clear,
                breathing_assessed,
                circulation_assessed,
                sats is not None and sats >= 88,
                map_value is not None and map_value >= 60,
                resp_rate is not None and resp_rate >= 8,
            ]
        )

        if all_stable:
            print(48)  # Finish
            break

        print(0)  # Do Nothing in absence of any direct action based on current knowledge

    except EOFError:
        break