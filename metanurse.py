while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check for airway clearing
    if events[3] > 0.5:  # AirwayClear confirmed
        airway_clear = True
    else:
        airway_clear = False
        print(3)  # ExamineAirway
        continue

    # Check breathing
    if events[7] > 0.5:  # BreathingNone significant
        print(29)  # UseBagValveMask
        continue
    elif measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Check circulation
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check disability (consciousness via AVPU)
    if (
        events[21] + events[22] + events[23] + events[24] == 0
    ):  # No AVPU response detected
        print(6)  # ExamineDisability
        continue

    # Exposure check for symptoms not handled by other checks
    if events[26] > 0.5 or events[27] > 0.5:  # Exposure issues like Shutdown or Stains
        print(7)  # ExamineExposure
        continue

    # Stabilization check
    if (
        airway_clear
        and (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[6] > 0 and measured_values[6] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    ):
        print(48)  # Finish the simulation
        break
    else:
        print(16)  # ViewMonitor if not all checks are cleared