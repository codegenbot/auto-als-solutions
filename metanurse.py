while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening checks
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measuredvalues[4] < 20):
        print(17)  # StartChestCompression
        continue
    
    # Check oxygen saturation
    if measured_times[5] == 0 or measured_times[5] < 0.5:
        print(25)  # UseSatsProbe
        continue
    
    # Airway check: Examine airway if not clear or not recently checked
    if events[3] < 0.5 and (events[4] + events[5] + events[6] > 0.5) or measured_times[0] == 0:
        print(3)  # ExamineAirway
        continue

    # Breathing issues: Manage if rate is low or specific conditions present
    measured_breathing = measured_times[6] > 0 and measured_values[6] >= 8
    if not measured_breathing:
        print(4)  # ExamineBreathing
        continue
    elif events[11] > 0.5 or events[14] > 0.5:  # Specific breathing issues
        print(22)  # BagDuringCPR if severe issues
        continue
    elif measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation Checks: If MAP not measured or low or conditions imply poor circulation
    if measured_times[4] == 0 or measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check if all parameters are within the target range to finish
    if (measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    # Set necessary measurements if any basic vital sign is critically unmeasured
    if measured_times[4] == 0:  # MAP not checked
        print(27)  # Bhagavi MenonUseBloodPressureCuff
    elif measured_times[6] == 0:  # Respiratory rate not measured
        print(4)  # ExamineBreathing
    else:
        print(16)  # ViewMonitor
    continue