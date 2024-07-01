airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
sats_probe_used = False
steps = 0
max_steps = 350

while steps < max_steps:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (
        events[6] > 0
        or (measured_times[5] > 0 and measured_values[5] < 65)
        or (measured_times[4] > 0 and measured_values[4] < 20)
    ):
        print(17)  # StartChestCompression for cardiac arrest condition
        continue

    if not airway_confirmed:
        if events[3] >= 0.1:  # AirwayClear
            airway_confirmed = True
            continue
        print(3)  # ExamineAirway
        continue

    if not sats_probe_used:
        print(25)  # UseSatsProbe
        sats_probe_used = True
        continue

    if not breathing_assessed:
        if measured_times[6] > 0:
            breathing_assessed = True
            continue
        print(4)  # ExamineBreathing
        continue

    if not circulation_checked:
        if events[16] >= 0.1 or events[17] >= 0.1:  # Pulse check
            circulation_checked = True
            continue
        print(5)  # ExamineCirculation
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask based on respiratory rate
        continue

    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask based on sats
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        print(38)  # TakeBloodPressure
        continue

    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish stabilizing patient
        break

    print(0)  # DoNothing as a last conditional resort