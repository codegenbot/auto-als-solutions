airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
initial_assessments_done = False
used_breathing_drawer = False
used_sats_probe = False
viewed_monitor_for_sats = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0.1:
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue
        if not breathing_assessed:
            if events[11] > 0 and (
                measured_times[5] == 0 or measured_values[5] < 88
            ):  # BreathingBibasalCrepitations observed
                if not used_breathing_drawer:
                    print(20)  # OpenBreathingDrawer
                    used_breathing_drawer = True
                    continue
                elif not used_sats_probe:
                    print(25)  # UseSatsProbe
                    used_sats_probe = True
                    continue
                elif not viewed_monitor_for_sats:
                    print(16)  # ViewMonitor
                    viewed_monitor_for_sats = True
                    continue
            else:
                print(4)  # ExamineBreathing
            breathing_assessed = True
            continue
        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue
        if not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue
        initial_assessments_done = True
        print(7)  # ExamineExposure
        continue

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
    else:
        if measured_times[5] == 0 or measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
        elif measured_times[4] == 0 or measured_values[4] < 60:
            if not used_breathing_drawer:
                print(20)  # OpenCirculationDrawer
                used_breathing_drawer = True
            else:
                print(14)  # UseVenflonIVCatheter
                print(15)  # GiveFluids
        else:
            print(16)  # ViewMonitor