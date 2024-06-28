while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Immediate Critical Interventions
    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  # StartChestCompression if sats critically low
            continue

    if times_recent_measure[4] > 0:
        if values[4] < 20:
            print(17)  # StartChestCompression if MAP critically low
            continue

    # Monitoring airway and breathing
    if events[3] + events[4] + events[5] + events[6] < 0.1:
        print(3)  # ExamineAirway
        continue

    if events[7] > 0.5 or (times_recent_measure[6] > 0 and values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Response to insufficient MAP
    if times_recent_measure[4] > 0 and values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check Cardiac Rhythms
    if events[38] > 0.5:  # HeartRhythmVF
        print(28)  # AttachDefibPads
        continue

    # Maintain and Monitor Sats
    if times_recent_measure[5] > 0:
        if values[5] < 88:
            print(30)  # UseNonRebreatherMask
        else:
            print(25)  # UseSatsProbe to confirm or update sats
        continue

    # All stabilizing conditions met
    if (
        times_recent_measure[5] > 0
        and values[5] >= 88
        and times_recent_measure[4] > 0
        and values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor, default safe action