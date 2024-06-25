while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    heart_rate = measurements[0] if times[0] > 0 else None

    critical_condition = (sats is not None and sats < 65) or (map_value is not None and map_value < 20)

    if critical_condition:
        if not events[38]:  # Defibrillator not on previously
            print(39)  # TurnOnDefibrillator
        elif not events[28]:  # Defib pads not attached
            print(28)  # AttachDefibPads
        else:
            print(17)  # StartChestCompression
        continue
    
    if not airway_clear:
        if events[5] or events[6]:  # AirwayVomit or AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
        else:
            print(3)  # ExamineAirway
        continue

    if sats is None or sats < 88:
        print(25)  # UseSatsProbe
        continue
    
    if map_value is None:
        print(27)  # UseBloodPressureCuff
        continue

    if resp_rate is None or resp_rate < 8:
        if events[29]:  # UseBagValveMask previously used
            print(22)  # BagDuringCPR
        else:
            print(29)  # UseBagValveMask
        continue

    if heart_rate is None or heart_rate < 60:
        print(16)  # ViewMonitor
        continue

    if map_value < 60:
        print(15)  # GiveFluids
        continue

    # Conditions met for finishing
    if sats >= 88 and map_value >= 60 and resp_rate >= 8 and heart_rate and heart_rate >= 60:
        print(48)  # Finish
        break

    # Default action if nothing else to perform
    print(0)  # DoNothing