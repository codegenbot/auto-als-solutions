while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and sats < 65 or (map_value is not None and map_column < 20):
        print(17)  # StartChestCompression
        continue

    # Emergency assessments
    if events[2] > 0:  # Non-verbal response detected, possible unconsciousness
        print(9)  # Use Jaw Thrust Maneuver
        continue
    elif events[7] > 0:  # BreathingNone detected
        print(29)  # Use Bag Valve Mask for assisted breathing
        continue

    # Airway check
    if events[3] + events[4] + events[5] + events[6] == 0:  # No recent airway checks
        print(3)  # ExamineAirway
        continue

    # Breathing and circulation check
    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask to increase oxygen
    elif map_value is not None and map_value < 60:
        print(15)  # Give Fluids to improve circulation

    # Regular checkups
    if events[0] == 0:  # No response verbal
        print(8)  # ExamineResponse
    elif events[6] == 0:  # No breathing equal chest expansion
        print(4)  # ExamineBreathing
    elif events[16] + events[17] == 0:  # No radial pulse check
        print(5)  # ExamineCirculation
    elif times[5] == 0:  # Sats not measured
        print(25)  # Use Sats Probe
    elif times[4] == 0:  # MAP not measured
        print(38)  # TakeBloodPressure
    elif events[36] > 0.1:  # Airway clear for a while
        print(3)  # ExamineAirway to reassess
    else:
        print(0)  # DoNothing in case of no immediate concern

    # Check if the patient is stabilized
    if sats is not None and sats >= 88 and map_value is not None and map_value >= 60 and resp_rate is not None and resp_rate >= 8:
        print(48)  # Finish - John is stabilized
        break
    else:
        print(0)  # Continue monitoring or addressing other issues