airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False

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
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if not breathing_assessed:
        if events[10] > 0.5:  # BreathingEqualChestExpansion observed
            breathing_assessed = True
            print(30)  # UseNonRebreatherMask
            print(25)  # UseSatsProbe
            print(16)  # ViewMonitor
            continue
        else:
            print(4)  # ExamineBreathing
            continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        print(16)  # ViewMonitor
        continue

    if measured_times[6] > 0 and (
        measured_values[6] < 8 or events[7] > 0.5
    ):  # Check respiration rate or breathing none available
        print(29)  # UseBagValveMask
        continue

    if not circulation_checked:
        if events[16] > 0.5 or events[17] > 0.5:  # Check palpable or non-palpable pulse
            circulation_checked = True
        print(5)  # ExamineCirculation
        continue

    if not disability_checked:
        if any(events[i] > 0.5 for i in range(21, 25)):  # Check AVPU responses
            disability_checked = True
        else:
            print(6)  # ExamineDisability
            continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0  # Sats at least 88
        and measured_values[6] >= 8
        and measured_times[4] > 0  # Resp Rate at least 8
        and measured_values[4] >= 60  # MAP at least 60
    ):
        print(48)  # Finish
        break

    print(16)  # ViewMonitor