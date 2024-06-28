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
        if events[17] > 0:  # RadialPulseNonPalpable
            print(17)  # StartChestCompression
        else:
            print(11)  # GiveAdrenaline
        step_count += 1
        continue

    # Checking and managing airway
    if not airway_clear_confirmed:
        if events[3] > 0:  # AirwayClear
            airway_clear_confirmed = True
        print(3)  # ExamineAirway
        step_count += 1
        continue

    # Breathing assessment and intervention
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:  # Check Saturation
        print(25)  # UseSatsProbe
        step_count += 1
        continue

    if events[8:14] == [0] * 6:  # Insufficient breathing assessment info
        print(4)  # ExamineBreathing
        step_count += 1
        continue

    # Circulation checks
    if measured_times[4] == 0 or measured_values[4] < 60:  # MAP not OK or not measured
        print(27)  # UseBloodPressureCuff
        step_count += 1
        continue

    # Circulation Management
    if events[16] > 0 and (events[17] > 0.5 or events[17] == 0):  # Pulse issues found or not measured
        print(5)  # ExamineCirculation
        step_count += 1
        continue

    # Disability assessment
    if events[21:24] == [0] * 3:  # AVPU not assessed
        print(6)  # ExamineDisability
        step_count += 1
        continue

    # Exposure evaluation
    if events[26] > 0.5:  # Suspects of Exposure issue
        print(7)  # ExamineExposure
        step_count += 1
        continue

    # Stabilization & Finish check
    if airway_clear_confirmed and measured_times[5] > 0 and measured_values[5] >= 88 and measured_times[6] > 0 and \
        measured_values[6] >= 8 and measured_times[4] > 0 and measured_values[4] >= 60:
        print(48)  # Finish
        break

    # Default action
    print(16)  # ViewMonitor
    step_count += 1