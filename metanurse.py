while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Critical condition, immediate response or exit
    if sats is not None and (sats < 65 or (map_value is not None and map_reset < 20)):
        print(17)  # Start Chest Compression
        continue

    # A: Airway assessment
    if events[3] <= 0.1:  # AirwayClear is not recent or strong
        print(3)  # Examine Airway
        continue

    # B: Breathing assessment
    if events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # C: Circulation assessment
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue
    if events[17] > 0.1:  # RadialPulseNonPalpable
        print(17)  # Start Chest Compression
        continue

    # D: Disability assessment
    if events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1:  # AVPU non-alert states
        print(6)  # Examine Disability
        continue

    # E: Exposure assessment
    print(7)  # Examine Exposure

    # Check if stabilized
    if (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_rate >= 8
    ):
        print(48)  # Finish
        break

    # Default action if none above taken
    print(0)  # DoNothing