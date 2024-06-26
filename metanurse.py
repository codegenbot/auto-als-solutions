import sys

step = 0
ABCDE_complete = {"A": False, "B": False, "C": False, "D": False, "E": False}

while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Handle immediately life-threatening conditions first
    if (sats is not None and sats < 65) or (map_value is not None and map_price < 20):
        print(17)  # StartChestCompression
        sys.stdout.flush()
        continue

    # Sequentially handle ABCDE with systematic approach
    if not ABCDE_complete["A"]:
        print(3)  # ExamineAirway
        ABCDE_complete["A"] = events[3] > 0.1
    elif not ABCDE_complete["B"]:
        if events[7] > 0.1:  # BreathingNone detected
            print(29)  # Use Bag Valve Mask
        else:
            print(4)  # ExamineBreathing
        ABCDE_complete["B"] = sats is not None and sats >= 88
    elif not ABCDE_complete["C"]:
        if map_value is None or map_value < 60:
            print(15)  # Give Fluids
        else:
            print(5)  # ExamineCirculation
        ABCDE_complete["C"] = map_value is not None and map_value >= 60
    elif not ABCDE_complete["D"]:
        print(6)  # ExamineDisability
        ABCDE_complete["D"] = True
    elif not ABCDE_complete["E"]:
        print(7)  # ExamineExposure
        ABCDE_complete["E"] = True
    else:
        # Check if all conditions for stabilization are met
        if (
            sats is not None
            and sats >= 88
            and resp_rate is not None
            and resp_rate >= 8
            and map_value is not None
            and map_value >= 60
            and events[3] > 0.1
        ):
            print(48)  # Finish - John is stabilized
            break
        else:
            # Reassess from the beginning if the patient is not stable
            ABCDE_complete = {
                "A": False,
                "B": False,
                "C": False,
                "D": False,
                "E": False,
            }

    step += 1
    if step >= 350:
        break

    sys.stdout.flush()