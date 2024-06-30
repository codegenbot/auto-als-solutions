steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if events[7] >= 0.7:
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not breathing_assessed and "Select the finger probe" in hint:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        continue

    if measured_values[5] < 88:  # Condition for low oxygen saturation
        print(30)  # UseNonRebreatherMask
        continue

    if measured_values[4] < 60:  # Low mean arterial pressure
        print(27)  # UseBloodPressureCuff
        continue

    if (
        events[25] == 0 or (measured_times[5] == 0 or measured_values[5] < 88)
    ) and not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

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

    print(0)  # DoNothing as last resort