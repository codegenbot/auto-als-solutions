airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_assessed = False

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

    if not airway_confirmed:
        if events[3] > 0:  # AirwayClear is True
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
        continue

    if not breathing_assessed:
        if events[10] > 0:  # BreathingEqualChestExpansion is True
            breathing_assessed = True
        else:
            print(4)  # ExamineBreathing
        continue

    if not circulation_checked:
        if events[16] > 0:  # RadialPulsePalpable is True
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
        continue

    if not disability_checked:
        if (
            events[21] > 0 or events[22] > 0 or events[23] > 0
        ):  # AVPU_A, AVPU_V, or AVPU_U is True
            disability_checked = True
        else:
            print(6)  # ExamineDisability
        continue

    if not exposure_assessed:
        print(7)  # ExamineExposure
        exposure_assessed = True
        continue

    if measured_times[4] <= 0:  # MAP not measured recently
        print(27)  # UseBloodPressureC_niluff
        continue

    if measured_times[5] <= 0:  # Sats not measured recently
        print(25)  # UseSatsProbe
        continue

    if (
        (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[6] > 0 and measured_values[6] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor