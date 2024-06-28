while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate response for no signs of life or dangerous levels
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway verification and management
    if events[2] > 0:  # ResponseNone
        print(3)  # ExamineAirway
        continue
    if events[4] > 0 or events[5] > 0 or events[6] > 0:  # AirwayBlockages
        print(32)  # UseGuedelAirway
        continue

    # Check if we need to get more information
    if measured_times[5] == 0:  # Sats not recently measured
        print(25)  # UseSatsProbe
        continue
    if measured_times[4] == 0:  # MAP not recently measured
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[6] == 0:  # Resp Rate not recently measured
        print(4)  # ExamineBreathing
        continue

    # Assess breathing
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Assess circulation and stabilize
    if measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Finish if patient is stabilized
    if measured_values[5] >= 88 and measured_values[6] >= 8 and measured_values[4] >= 60:
        print(48)  # Finish
        break

    # Default action to keep the loop active
    print(0)  # DoNothing