airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False
steps = 0


def get_vitals(measurements, times):
    sats = measurements[5] if times[5] > 0 else None
    map = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    return sats, map, resp_rate


while steps < 350:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats, map, resp_rate = get_vitals(measurements, times)

        if sats is not None and sats < 65 or map is not None and map < 20:
            print(17)  # Start Chest Compression
            continue

        if not airway_checked or not airway_clear:
            print(3)  # Examine Airway
            airway_checked = True
            airway_clear = events[3] > 0.1  # AirwayClear has significant relevance
            continue

        if not breathing_assessed:
            if events[7] > 0.1:  # BreathingNone significant relevance
                print(29)  # Use Bag Valve Mask
                breathing_assessed = True
                continue

        if airway_clear:
            if not circulation_assessed:
                if sats is not None and sats < 88:
                    print(30)  # Use Non Rebreather Mask
                elif map is not None and map < 60:
                    print(15)  # Give Fluids
                circulation_assessed = True
                continue

        if airway_clear and breathing_assessed and circulation_assessed:
            if (
                sats is not None
                and sats >= 88
                and map is not None
                and map >= 60
                and (resp_rate is not None and resp_rate >= 8)
            ):
                print(48)  # Finish
                break

        print(
            0
        )  # Do Nothing in absence of any direct action based on current knowledge

        steps += 1
    except EOFError:
        break