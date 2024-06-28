def decide_action(events, times_recent_measure, values):
    if events[7] > 0:  # If there's indication of no breathing
        return 29  # UseBagValveMask
    if not any(events[:6]):  # If no recent airway check
        return 3  # ExamineAirway
    if not any(events[8:14]):  # If no recent breathing check
        return 4  # ExamineBreating
    if not any(events[15:24]):  # If no recent circulation check
        return 5  # ExamineCirculation
    if not any(events[24:27]):  # If no 'D' examination conducted
        return 6  # ExamineDisability
    if not any(events[27:33]):  # If no 'E' examination conducted
        return 7  # ExamineExposure

    if times_recent_measure[5] > 0 and values[5] < 88:
        return 30  # UseNonRebreatherMask
    if times_recent_measure[4] > 0 and values[4] < 60:
        return 15  # GiveFluids

    # Finalize if stable
    if (
        times_recent_measure[5] > 0
        and values[5] >= 88
        and times_recent_measure[6] > 0
        and values[6] >= 8
        and times_recent_measure[4] > 0
        and values[4] >= 60
    ):
        return 48  # Finish

    return 16  # ViewMonitor for general case


# Main loop for treatment
while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))
    action = decide_action(events, times_recent_measure, values)
    print(action)
    if action == 48:  # Finish
        break