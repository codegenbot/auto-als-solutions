airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False
resp_rate_assessed = False

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

        if not airway_checked:
            print(3)  # Examine Airway
            airway_checked = True
            continue

        if events[5] > 0.1:  # AirwayBlood
            print(31)  # Use Yankeur Suction Catheter
            continue

        if not breathing_assessed and (
            events[7] > 0.1 or events[8] > 0.1 or events[9] > 0.1
        ):  # BreathingNone, BreathingSnoring, BreathingSeeSaw
            print(29)  # Use Bag Valve Mask
            breathing_assessed = True
            continue
        elif events[10] <= 0.1:
            print(4)  # Examine Breathing
            continue

        if not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            continue

        if map_value is None or map_value < 60:
            print(15)  # Give Fluids
            continue
        if sats is None or sats < 88:
            print(30)  # Use Non Rebreather Mask
            continue
        if resp_rate is None or resp_rate < 8:
            print(29)  # Use Bag Valve Mask
            resp_rate_assessed = True
            continue

        if all(
            [
                airway_clear,
                sats is not None and sats >= 88,
                resp_rate is not None and resp_rate >= 8,
                map_value is not None and map_value >= 60,
            ]
        ):
            print(48)  # Finish
            break

        print(0)  # Do Nothing as default action

    except EOFError:
        break