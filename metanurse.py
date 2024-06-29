airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
measurements_updated = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if not breathing_assessed and events[3] > 0:  # AirwayClear detected
        airway_confirmed = True
        print(4)  # ExamineBreathing
        continue

    if (
        not circulation_checked and events[10] > 0
    ):  # BreathingEqualChestExpansion detected
        breathing_assessed = True
        print(5)  # ExamineCirculation
        continue

    if not disability_checked and events[16] > 0:  # RadialPulsePalpable detected
        circulation_checked = True
        print(6)  # ExamineDisability
        continue

    if disability_checked and (
        events[23] > 0 or events[24] > 0
    ):  # PupilsPinpoint or PupilsNormal detected
        disability_checked = True
        measurements_updated = True

    if measured_times[4] <= 0:  # Blood pressure not measured recently
        print(27)  # UseBloodPressureCuff
        continue

    if measured_times[5] <= 0:  # Sats not measured recently
        print(25)  # UseSatsProbe
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if (
        measurements_updated
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor