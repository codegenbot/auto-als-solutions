previous_actions = set()

while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate Response to Critical Conditions
    if sats is not None and sats < 65:
        if 17 not in previous_actions:
            print(17)  # Start Chest Compression
            continue
    if map_value is not None and map_value < 20:
        if 17 not in previous_actions:
            print(17)  # Start Chest Compression
            continue

    # Airway Management
    if events[3] < 0.1 and 3 not in previous_actions:  # Airway not recently checked
        print(3)  # Examine Airway
        previous_actions.add(3)
        continue
    if (
        events[4] > 0.1 or events[5] > 0.1
    ) and 31 not in previous_actions:  # Presence of Vomit or Blood
        print(31)  # Use Yankeur Suction Catheter
        previous_actions.add(31)
        continue
    if events[6] > 0.1 and 36 not in previous_actions:
        print(36)  # PerformHeadTiltChinLift
        previous_actions.add(36)
        continue

    # Breathing Assessment
    if events[7] > 0.1 and 29 not in previous_actions:  # Breathing None
        print(29)  # Use Bag Valve Mask
        previous_actions.add(29)
        continue

    # Circulation Check
    if (
        events[28] > 0.1 or events[30] > 0.1
    ) and 28 not in previous_actions:  # Dangerous heart rhythms
        print(28)  # Attach Defib Pads
        previous_actions.add(28)
        continue

    # Stabilizing Measures
    if sats is not None and sats < 88 and 30 not in previous_actions:
        print(30)  # Use Non Rebreather Mask
        previous_actions.add(30)
        continue
    if map_value is not None and map_value < 60 and 15 not in previous_actions:
        print(15)  # Give Fluids
        previous_actions.add(15)
        continue

    # Ongoing Monitoring and Responsive Actions
    if not previous_actions and times[5] == 0:
        print(25)  # UseSatsProbe
        previous_actions.add(25)
        continue
    if times[4] == 0 and 27 not in previous_actions:
        print(27)  # UseBloodPressureCuff
        previous_actions.add(27)
        continue
    if (
        not (events[7] > 0.1) and 4 not in previous_actions
    ):  # if breathing not already managed
        print(4)  # Examine Breathing
        previous_actions.add(4)
        continue

    # Continuously look for new data and re-assess situation
    if 16 not in previous_actions:
        print(16)  # View Monitor for updates
        previous_actions.add(16)
        continue

    # Check patient stability and finalize if stable
    if (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_rate >= 8
    ):
        print(48)  # Finish Scenario
        break

    # Default action if no critical actions are required
    previous_actions.clear()  # Clear past actions to allow re-checking
    print(0)  # DoNothing, continue monitoring