airway_checked = False
airway_clear = False
breathing_assessed = False
cycle_started = False
vitals_checked = False
circulation_assessed = False

def get_vitals(measurements, times):
    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    return sats, map_value, resp_rate

while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats, map_value, resp_rate = get_vitals(measurements, times)

        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            if not cycle_started:
                print(17)  # Start Chest Compression
                cycle_started = True
                continue

        if sats is not None and (sats < 88 or sats >= 65):
            print(30)  # Use Non Rebreather Mask
            continue

        if map_value is not None and map_value < 60:
            print(15)  # Give Fluids
            circulation_assessed = True
            continue

        if not airway_checked or not airway_clear:
            print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0.1  # AirwayClear has significant relevance, event[3] - AirwayClear
            continue

        if not vitals_checked:
            print(25)  # UseSatsProbe
            print(27)  # UseBloodPressureCuff
            vitals_checked = True
            continue

        if not breathing_assessed:
            print(4)  # Examine Breathing
            breathing_assessed = True
            continue

        if not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            continue

        if cycle_started:
            print(23)  # ResumeCPR
            continue

        all_stable = all([
            sats is not None and sats >= 88,
            map_value is not None and map_value >= 60,
            resp_rate is not or resp_rate >= 8,
            airway_clear
        ])

        if all_stable:
            print(48)  # Finish
            break

        print(0)  # Do Nothing in absence of any direct action based on current knowledge

    except EOFError:
        break