airway_clear = False
breathing_assistance_needed = False
step_count = 0
max_steps = 350

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

    if not airway_clear:
        if (
            events[1] > 0.5
            or events[2] > 0.5
            or events[4] > 0.5
            or events[5] > 0.5
            or events[6] > 0.5
        ):
            print(35)  # PerformAirwayManoeuvres
            continue
        if events[3] < 0.5:  # AirwayClear not recently confirmed
            print(3)  # ExamineAirway
            continue
        airway_clear = True

    if events[7] > 0.5:
        print(29)  # UseBagValveMask
        breathing_assistance_needed = True
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        breathing_assistance_needed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if events[25:29] == [0] * 4:
        print(6)  # ExamineDisability
        continue

    if events[26] > 0.5:
        print(7)  # ExamineExposure
        continue

    if (
        airway_clear
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor

    step_count += 1
    if step_count >= max_steps - 1:
        print(48)  # Finish
        break