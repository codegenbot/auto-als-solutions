while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    # Immediate life-threatening conditions check
    if sats is not None and sats < 65 or (map_value is not None and map_dict < 20):
        print(17)  # StartChestCompression
        continue

    # Airway assessment
    if events[3] <= 0.1:  # Low relevance of AirwayClear, indicating need to examine
        print(3)  # ExamineAirway
    elif events[7] > 0.1:  # BreathingNone detected
        print(29)  # Use Bag Valve Mask for assisted breathing
    elif sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask to increase oxygen

    # Circulation assessment
    elif map_value is None or map_value < 60:
        print(5)  # ExamineCirculation if not examined or if MAP is low
    elif events[17] == 0:  # RadialPulseNonPalpable
        print(17)  # StartChestCompression

    # Disability (Consciousness)
    elif events[21] > 0.1 or events[22] > 0.1:  # AVPU_U or AVPU_V low relevance
        print(6)  # ExamineDisability

    # Exposure
    elif (
        events[25] <= 0.1 or events[26] <= 0.1
    ):  # Exposure Rashes or Peripheral Shutdown
        print(7)  # ExamineExposure

    # Respiratory rate reassessment
    elif resp_rate is not None and resp_rate < 8:
        print(4)  # ExamineBreathing

    # Stabilization check
    elif (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map_value >= 60
        and resp_rate is not None
        and resp_rate >= 8
        and events[3] > 0.1  # Airway is clear
    ):
        print(48)  # Finish - John is stabilized
        break
    else:
        print(0)  # DoNothing