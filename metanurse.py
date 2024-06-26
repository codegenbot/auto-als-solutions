step = 0

while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Check critical conditions
    if sats is not None and (sats < 65 or (map_value is not None and map_value < 20)):
        print(17)  # StartChestCompression
        continue

    # Airway management
    if events[3] <= 0.1:  # Low relevance of AirwayClear event
        print(3)  # Examine Airway
        continue

    # Breathing management
    if events[7] > 0.1:  # BreathingNone detected
        print(29)  # Use Bag Valve Mask
        continue

    # Use high oxygen if saturation low
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    # Circulation remediation if necessary
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    # Check breathing if rate is too low
    if resp_rate is not None and resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    # Check for stabilization
    if (
        (sats is not None and sats >= 88)
        and (map_value is not None and map_value >= 60)
        and (resp_rate is not None and resp_rate >= 8)
        and events[3] > 0.1  # Airway clear
    ):
        print(48)  # Finish
        break

    # Default safe action to gather more data
    if step % 5 == 0:
        print(16)  # ViewMonitor
    else:
        print(0)  # DoNothing

    step += 1
    if step > 350:
        break