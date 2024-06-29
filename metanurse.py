def main():
    step_count = 0
    airway_confirmed = False
    breathing_assessed = False
    circulation_checked = False
    disability_checked = False

    while step_count < 350:
        observations = input().split()
        events = list(map(float, observations[:39]))
        measured_times = list(map(float, observations[39:46]))
        measured_values = list(map(float, observations[46:]))

        if (measured_times[5] > 0 and measured_values[5] < 65) or (
            measured_times[4] > 0 and measured_values[4] < 20
        ):
            print(17)  # StartChestCompression
        elif events[7] == 1:  # BreathingNone
            print(29)  # UseBagValveMask
        elif not airway_confirmed:
            print(3)  # ExamineAirway
        elif not breathing_assessed:
            print(4)  # ExamineBreathing
        elif not circulation_checked:
            print(5)  # ExamineCirculation
        elif measured_times[4] <= 0:  # Check if BP not measured
            print(27)  # UseBloodPressureCuff
        elif measured_times[5] <= 0:  # Check if Sats not measured
            print(25)  # UseSatsProbe
        elif (
            measured_values[4] >= 60
            and measured_values[5] >= 88
            and measured_values[6] >= 8
        ):
            print(48)  # Finish
        else:
            print(16)  # ViewMonitor

        step_count += 1
        if step_count >= 350:
            print(48)  # Finish
            break


if __name__ == "__main__":
    main()