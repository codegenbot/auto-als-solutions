while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and (sats < 65 or (map_value is not None and map_value < 20)):
        print(17)  # StartChestCompression
        continue

    if events[4] or events[5] or events[6]:  # AirwayVomit, AirwayBlood, or AirwayTongue
        print(31)  # UseYankeurSuctionCatheter
        continue
    elif events[3] <= 0.1:  # Airway not clear
        print(3)  # ExamineAirway
        continue

    if events[7] > 0.1:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    elif events[10] <= 0.1:  # Breathing not equal
        print(4)  # ExamineBreathing
        continue

    if events[17] > 0.1:  # RadialPulseNonPalpable
        print(15)  # GiveFluids
        continue
    if map_value is not None and map_value < 60:
        print(15)  # GiveFluids
        continue

    if events[22] > 0.1 or events[21] > 0.1:  # AVPU_V or AVPU_U
        print(6)  # ExamineDisability
        continue

    if times[8] <= 0.1:  # less frequent checks
        print(7)  # ExamineExposure
        continue

    if times[5] <= 0.1:  # Sats not recently measured
        print(25)  # UseSatsProbe
        continue
    if times[4] <= 0.1:  # MAP not recently measured
        print(27)  # UseBloodPressureCuff
        continue

    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and map_value >= 60)
        and (resp_rate is not None and resp_rate >= 8)
        and events[3] > 0.1  # AirwayClear
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing