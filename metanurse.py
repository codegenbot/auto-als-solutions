while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions for cardiac arrest
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway check and management
    if (
        events[3] < 0.5 and events[4] == 0 and events[5] == 0 and events[6] == 0
    ):  # Airway unclear
        print(3)  # ExamineAirway
        continue
    elif (
        events[4] > 0 or events[5] > 0 or events[6] > 0
    ):  # Obstructions like vomit, blood, tongue
        print(35)  # PerformAirwayManoeuvres
        continue

    # Breathing support and interventions
    if events[7] > 0.5:  # Emergency in breathing
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation: check and maintain
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Checking disability: consciousness level
    if events[22] > 0.5 or events[22] > 0.5:  # Unresponsive to voice or unresponsive
        print(6)  # ExamineDisability
        continue

    # Exposure: check for other signs influencing state
    if events[26] > 0.5:  # Exposure with signs like shutdown
        print(7)  # ExamineExposure
        continue

    # Regular monitoring and reassess
    if (
        events[25] == 0 and events[26] == 0 and events[27] == 0
    ):  # Normal pupils, no clear shutdown or staining
        print(16)  # ViewMonitor
        continue

    # Final check before finishing once stabilized
    if measured_times[5] > 0 and measured_values[6] > 0 and measured_times[4] > 0:
        if (
            measured_values[5] >= 88
            and measured_values[6] >= 8
            and measured_values[4] >= 60
        ):
            print(48)  # Finish
            break