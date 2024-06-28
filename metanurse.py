step_count = 0
max_steps = 350
airway_clear = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if step_count >= max_steps - 1:
        print(48)  # Finish
        break

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        step_count += 1
        continue

    if not airway_clear:
        if events[3] < 0.1:  # Airway not checked or clear
            print(3)  # ExamineAirway
            step_count += 1
            continue
        if events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:  # Airway obstructions
            print(35)  # PerformAirwayManoeuvres
            step_count += 1
            continue
        airway_clear = True

    if events[7] > 0.5:  # No Breathing
        print(29)  # UseBagValveMask
        step_count += 1
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:  # Low oxygen saturation
        print(30)  # UseNonRebreatherMask
        step_count += 1
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:  # Low respiratory rate
        print(29)  # UseBagValveMask
        step_count += 1
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:  # Low mean arterial pressure
        print(15)  # GiveFluids
        step_count += 1
        continue

    if events[25:29] == [0] * 4:  # Check disability if no response events have occurred
        print(6)  # ExamineDisability
        step_count += 1
        continue

    if events[26] > 0.5 or events[27] > 0.5:  # Exposure issues
        print(7)  # ExamineExposure
        step_count += 1
        continue

    print(16)  # ViewMonitor
    step_df += 1
    if step_count % 10 == 0:  # Periodic comprehensive examination
        print(4)  # ExamineBreathing
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