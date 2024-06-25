state_tracker = {
    "AirwayChecked": False,
    "BreathingChecked": False,
    "CirculationChecked": False,
    "DisabilityChecked": False,
    "ExposureChecked": False
}

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
            print(17)  # Start Chest Compression
            continue

        if events[7] > 0.1:  # BreathingNone significant
            if events[17] > 0.1:  # RadialPulseNonPalpable significant
                print(17)  # Start Chest Compression
            else:
                print(29)  # Use Bag Valve Mask
        elif events[17] > 0.1:  # RadialPulseNonPalpable significant
            print(17)  # Start Chest Compression
            continue

        if not state_tracker["AirwayChecked"]:
            print(3)  # ExamineAirway
            state_tracker["AirwayChecked"] = True
        elif not state_tracker["BreathingChecked"]:
            print(4)  # ExamineBreathing
            state_tracker["BreathingChecked"] = True
        elif not state_tracker["CirculationChecked"]:
            print(5)  # ExamineCirculation
            state_tracker["CirculationChecked"] = True
        elif not state_tracker["DisabilityChecked"]:
            print(6)  # ExamineDisability
            state_tracker["DisabilityChecked"] = True
        elif not state_id":
            print(7)  # ExposureChecked"] and events[1] > 0.1 (i.e., ResponseVerbal is significant)
            print(7)  # ExamineExposure
            state_tracker["ExposureChecked"] = True
        else:
            if sats is not None and sats < 88:
                print(30)  # Use Non Rebreather Mask
            elif map_value is not None and map_value < 60:
                print(15)  # Give Fluids
            elif resp_rate is not None and resp_rate < 8:
                print(29)  # Use Bag Valve Mask
            elif all(state_tracker.values()):
                print(48)  # Finish
                break
            else:
                print(0)  # Do Nothing if no other conditional matches

    except EOFError:
        break