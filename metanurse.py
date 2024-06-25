airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False
resp_rate_checked = False
saturation_checked = False

while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start Chest Compression
            continue

        if events[7] > 0.1:  # BreathingNone significant relevance
            print(17)  # Start Chest Compression
            continue

        if (
            not airway_checked or events[3] <= 0.1
        ):  # AirwayClear has no significant relevance
            print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0.1
            continue

        if not breathing_assessed:
            print(4)  # Examine Breathing
            breathing_assessed = True
            continue

        if not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            continue

        if not resp_rate_checked and (resp_rate is None or resp_rate < 8):
            print(38)  # Take Blood Pressure
            resp_rate_checked = True
            continue

        if not saturation_checked and (sats is None or sats < 88):
            print(25)  # Use Sats Probe
            saturation_checked = True
            continue

        all_stable = all(
            [
                airway_checked,
                airway_clear,
                breathing_assessed,
                circulation_assessed,
                resp_rate_checked,
                saturation_checked,
                sats is not None and sats >= 88,
                map_value is not None and map_value >= 60,
                resp_rate is not None and resp_rate >= 8,
            ]
        )

        if all_stable:
            print(48)  # Finish
            break

        print(
            0
        )  # Do Nothing in absence of any direct action based on current knowledge

    except EOFError:
        break