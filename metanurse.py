airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False

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
            print(17)  # StartChestCompression
            continue

        if not airway_checked:
            print(3)  # ExamineAirway
            airway_checked = True
            continue

        if events[3] <= 0.1:  # AirwayClear positive
            airway_clear = True
        elif events[4] > 0.1 or events[5] > 0.1:  # AirwayVomit or AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
            continue

        if not breathing_assessed and airway_clear:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

        if events[7] > 0.1:  # BreathingNone is significant
            print(29)  # UseBagValveMask
            continue

        if sats is not None and sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if not circulation_assessed and airway_clear and breathing_assessed:
            print(5)  # ExamineCirculation
            circulation_assessed = True
            continue

        if map_value is not None and map_value < 60:
            print(15)  # GiveFluids
            continue

        if sats is None:
            print(25)  # UseSatsProbe
            continue

        if map_value is None:
            print(27)  # UseBloodPressureCuff
            continue

        all_stable = (
            airway_clear
            and breathing_assessed
            and circulation_assessed
            and sats is not None
            and sats >= 88
            and map_value is not None
            and map_view >= 60
            and resp_rate is not None
            and resp_rate >= 8
        )

        if all_stable:
            print(48)  # Finish
            break

        print(0)  # DoNothing if none of the above conditions met

    except EOFError:
        break