step = 0

while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Critical condition check for immediate life-threatening events
    if (sats is not None and sats < 65) or (map_value is not None and map_ratio < 20):
        print(17)  # StartChestCompression
        continue

    # ABCDE systematic checks
    if step % 5 == 0:
        print(3)  # ExamineAirway
    elif step % 5 == 1:
        if events[7] <= 0.1:  # Breathing issues not detected yet
            print(4)  # ExamineBreathing
        else:
            print(29)  # Use Bag Valve Mask for breathing issues
    elif step % 5 == 2:
        print(5)  # ExamineCirculation
    elif step % 5 == 3:
        print(6)  # ExamineDisability
    elif step % 5 == 4:
        print(7)  # ExamineExposure

    step += 1

    # Check if patient is stabilized
    if (sats is not None and sats >= 88 and
        map_value is not None and map_value >= 60 and
        resp_rate is not None and resp_rate >= 8 and
        events[3] > 0.1):  # Airway is clear
        print(48)  # Finish - John is stabilized
        break

    if step >= 350:
        print(48)  # Force finish after 350 steps, should not normally be needed
        break

    # Additional actions based on urgent needs, improve other measurements
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask to increase oxygen
        continue
    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue
    if resp_rate is not None and resp_rate < 8:
        print(29)  # Use Bag Valve Mask if breathing is critically low
        continue

    print(0)  # Default action when no immediate action is concluded