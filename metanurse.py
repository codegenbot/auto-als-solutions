while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical condition checks
    if events[7] > 0 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    # Airway examination
    if not airway_confirmed:
        if events[3] > 0.1:  # AirwayClear
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing examination
    if not breathing_assessed:
        if events[12] > 0 or events[13] > 0:
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
            continue

    # For circulation, ensure pulse can be felt
    if not circulation_checked:
        if events[16] > 0:  # RadialPulsePalpable
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    # If breathing observations indicate insufficient oxygen levels, use non-rebreather mask or similar interventions
    if measured_times[5] > 0 and measured_values[5] < 88:
        if not satsProbeUsed:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue
        print(30)  # UseNonRebreatherMask
        continue

    # Final check before finishing
    if airway_confirmed and breathing_assessed and circulation_checked:
        if measured_times[5] > 0 and measured_values[5] >= 88\
           and measured_times[6] > 0 and measured_values[6] >= 8\
           and measured_times[4] > 0 and measured_values[4] >= 60:
            print(48)  # Finish
            break

    print(0)  # DoNothing as fallback