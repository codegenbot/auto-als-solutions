while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # High priority: Handle risk of cardiac arrest immediately
    if sats is not None and sats < 65:
        print(17)  # Start Chest Compression
        continue
    if map_value is not None and map_value < 20:
        print(17)  # Start Chest Compression
        continue

    # Step 1: Airway check and clearance if needed
    if events[3] <= 0.1:  # AirwayClear has low relevance
        if events[5] > 0:  # AirwayVomit
            print(31)  # Use Yankeur Suction Catheter
            continue
        elif events[6] > 0:  # AirwayBlood
            print(31)  # Use Yankeur Suction Catheter
            continue
        elif events[7] > 0:  # AirwayTongue observed
            print(32)  # Use Guedel Airway
            continue
        else:
            print(3)  # Examine Airway
            continue

    # Step 2: Breathing and ventilation
    if events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue

    # Step 3: Circulation check
    if (events[17] > 0 or events[16] <= 0.1) and times[
        4
    ] <= 0.1:  # RadialPulseNonPalpable or RadialPulsePalpable low relevance
        print(5)  # Examine Circulation
        continue
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Step 4: Disability - consciousness check
    if (
        events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1
    ):  # AVPU_U or AVPU_V or AVPU_P (non-alert states)
        print(8)  # Examine Response
        continue

    # Step 5: Exposure - check underlying causes
    print(7)  # ExamineExposure

    # Step 6: Ensure stabilization criteria
    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and map_value >= 60)
        and (resp_rate is not None and resp_color >= 8)
    ):
        print(48)  # Finish
        break

    # Default Action: Check vital signs frequently
    if times[5] <= 0.1:  # Saturation was measured recently
        print(25)  # Use Sats Probe
    elif times[4] <= 0.1:  # MAP was measured recently
        print(27)  # Use Blood Pressure Cuff
    else:
        print(16)  # View monitor for a comprehensive check