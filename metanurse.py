while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Assess response and airway immediately
    if events[2] > 0:  # ResponseNone
        print(3)  # ExamineAirway
        continue

    # Critical immediate actions
    if events[7] > 0:  # BreathingNone
        print(17)  # StartChestCompression
        continue
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Examine airway and breathing
    if events[4] > 0:  # Airway blockage like AirwayVomit
        print(32)  # UseGuedelAirway
        continue
    if events[6] > 0:  # AirwayBlood
        print(32)  # UseGuedelAirway
        continue

    # Check for breathing issues
    if events[7] > 0 and events[14] == 0:  # BreathingNone without Pneumothorax
        print(29)  # UseBagValveMask
        continue
    if events[14] > 0:  # Pneumothorax Symptoms
        print(0)  # Consider emergency intervention
        continue

    # Re-check necessary vitals:
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Circulation issues
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Saturations and respiratory rate
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Stabilization check
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default action if no immediate issues
    print(0)  # DoNothing