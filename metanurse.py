airway_checked = False
while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical Immediate Actions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if (
        not airway_checked or events[4] > 0 or events[5] > 0
    ):  # Check if airway not checked or there are signs of blockage
        print(3)  # ExamineAirway
        airway_checked = True
        continue

    # Stability check before finishing
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

    # If unsure, perform next logical step in ABCDE
    # Implement logic to determine next undiscovered issue...