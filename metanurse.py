airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False

step_count = 0

while step_count < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions handling
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        step_count += 1
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        step_count += 1
        continue

    # ABCDE Assessment sequence
    if not airway_confirmed:
        print(3)  # ExamineAirway
        airway_confirmed = (
            events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0
        )
        step_count += 1
        continue

    if not breathing_assessed and airway_confirmed:
        print(4)  # ExamineBreathing
        breathing_assessed = (
            events[10] > 0 or events[13] > 0 or events[14] > 0
        )  # Assuming these events can confirm breathing state
        step_count += 1
        continue

    if not circulation_checked and breathing_assessed:
        print(5)  # ExamineCirculation
        circulation_checked = (
            events[16] > 0
        )  # RadialPulsePalpable indicates circulation
        step_count += 1
        continue

    if not disability_checked and circulation_checked:
        print(6)  # ExamineDisability
        disability_checked = (
            events[22] > 0 or events[23] > 0 or events[24] > 0
        )  # Based on AVPU responses & pupil status
        step_count += 1
        continue

    if measured_times[4] <= 0:  # Blood pressure not measured recently
        print(27)  # UseBloodPressureCuff
        step_count += 1
        continue

    if measured_times[5] <= 0:  # Sats not measured recently
        print(25)  # UseSatsProbe
        step_count += 1
        continue

    # Check stabilization condition
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    step_count += 1
    print(16)  # ViewMonitor if nothing else is needed