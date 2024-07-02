steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if events[7] > 0:
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            continue
        # Follow with other initial examinations in similar structure...

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids assuming "15" is correction for such condition
        continue

    if (
        airway_confirmed
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing as a default if none of the above conditions are met