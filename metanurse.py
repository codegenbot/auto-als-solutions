airway_clear_confirmed = False
step_count = 0

while step_count < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Handling Cardiac Arrest or Severe Conditions Immediately
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        step_count += 1
        continue

    # Directly address airway clearness
    if not airway_clear_confirmed or events[4] > 0 or events[5] > 0 or events[6] > 0:
        print(3)  # ExamineAirway to verify and clear it
        step_count += 1
        continue

    # Breathing assessment: use masks or check with ExamineBreathing
    if measured_times[6] > 0 and measured_values[6] < 8 or events[7] > 0:
        print(29)  # Insufficient breathing, use bag valve mask
        step_count += 1
        continue

    # Circulation issues: weak pulse, administer fluids or chest compressions
    if measured_times[4] > 0 and measured_values[4] < 60 or events[17] > 0:
        print(15)  # Administer fluids for possible low BP/circulation
        step_count += 1
        continue

    # Check Disability (consciousness level) and Exposure if not assessed yet
    if events[21:24] == [0] * 3:
        print(6)  # ExamineDisability for consciousness level
        step_count += 1
        continue

    # Finally, if patient appears stabilized:
    if (
        airway_clear_confirmed
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish the scenario
        break

    # Default action periodically to monitor vital stats
    print(16)  # ViewMonitor
    step_count += 1