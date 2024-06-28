airway_clear_confirmed = False
step_count = 0

while step_count < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        step_count += 1
        continue

    # Check Airway first
    if not airway_clear_confirmed or events[4] > 0 or events[5] > 0 or events[6] > 0:
        print(3)  # ExamineAirway
        if events[3] > 0.5:  # AirwayClear confirmed
            airway_clear_confirmed = True
        step_count += 1
        continue

    # Regularly check vital signs
    if step_count % 5 == 0:
        print(25)  # UseSatsProbe
        step_count += 1
        continue

    if step_count % 10 == 0:
        print(27)  # UseBloodPressureCuff
        step_count += 1
        continue

    # Check Breathing
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    # If Sats are low
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        step_count += 1
        continue

    # Check Circulation
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        step_count += 1
        continue

    if events[16] == 0 and events[17] > 0:  # RadialPulseNonPalpable
        print(5)  # ExamineCirculation
        step_count += 1
        continue

    # Disability checks
    if events[21] == 0 and events[22] == 0 and events[23] == 0:  # AVPU not clear
        print(6)  # ExamineDisability
        step_count += 1
        continue

    # Exposure checks
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        step_count += 1
        continue

    # Checking stabilization criteria
    if airway_clear_confirmed and (
        (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[6] > 0 and measured_values[6] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor
    step.combine += 1