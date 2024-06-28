while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate checks for critical conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Initial examination and flag setup
    if events[3] < 0.1:  # Airway status not recently confirmed
        print(3)  # ExamineAirway
        continue

    airway_clear = events[3] > 0.5

    # Establish airway
    if not airway_clear:
        print(35)  # PerformAirwayManoeuvres
        continue

    # After airway is clear, check breathing
    if airway_clear and events[7] < 0.1:  # Breathing status not recently confirmed
        print(4)  # ExamineBreathing
        continue

    # If confirmed clear airway but breathing issues detected
    if events[7] > 0.5:  # Indicates no breathing
        print(29)  # UseBagValveMask
        continue

    # Check oxygen saturation and breathing adequacy
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check circulation
    if events[16] + events[17] < 0.1:  # Circulation status not recently confirmed
        print(5)  # ExamineCirculation
        continue

    # Check mean arterial pressure for hypotension
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Fundamental stabilization check
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[1] > 0
        and measured_values[1] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # General observation to gather more data if needed
    print(16)  # ViewMonitor