while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Check life-threatening conditions first
    if sats is not None and sats < 65:
        print(17)  # StartChestCompression
        continue
    if map_value is not None and map_value < 20:
        print(17)  # StartChestCompression
        continue

    # Examine airway if not recently checked or problems suspected
    if events[3] <= 0.1 or events[5] > 0 or events[6] > 0 or events[4] > 0:  # Airway problems
        print(3)  # Examine Airway
        continue

    # Ensure good breathing
    if events[7] > 0.1:  # BreathingNone
        print(29)  # Use Bag Valve Mask
        continue
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Check circulation
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Check respiratory rate
    if resp_rate is not None and resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    # Check vital signs periodically
    if times[5] == 0:  # Sats not measured
        print(25)  # UseSatsProbe
        continue
    if times[4] == 0:  # MAP not measured
        print(38)  # TakeBloodPressure
        continue

    # End condition
    if (sats is not None and sats >= 88) and (map_value is not None and map_value >= 60) and (resp_rate is not None and resp_rate >= 8):
        print(48)  # Finish
        break

    # Default action if no immediate issues are detected
    print(0)  # DoNothing