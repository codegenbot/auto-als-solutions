while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions management
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Assess airway
    if events[2] > 0:  # ResponseNone
        print(3)  # ExamineAirway
        continue

    # Manage airway obstructions
    if (
        events[4] > 0 or events[5] > 0 or events[6] > 0
    ):  # AirwayVomit, AirwayBlood, AirwayTongue
        print(32)  # UseGuedelAirway
        continue

    # Manage breathing issues
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Check vital signs if not recently measured
    if measured_times[4] == 0 or measured_times[5] == 0 or measured_times[6] == 0:
        print(16)  # ViewMonitor
        continue

    # Fluids for circulation issues
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Oxygen management
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check if the patient is stabilised
    if (
        measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    # Default action
    print(0)  # DoNothing